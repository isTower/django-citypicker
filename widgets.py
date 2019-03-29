#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Time    : 2019/3/29 17:38
# @Author  : Money
# @Site    : 
# @File    : widgets.py
# @Software: PyCharm


from django import forms
from django.utils.safestring import mark_safe


try:
    from django.forms.widgets import get_default_renderer
except ImportError:
    from django.forms.renderers import get_default_renderer


class CityPickerWidget(forms.Textarea):

    class Media:
        css = {
            "all": (
                "css/city-picker.css",
                "css/main.css")
        }
        js = (
            "js/city-picker.data.js",
            "js/city-picker.js",
            "js/main.js"
        )

    def __init__(self, config_name='default',*args, **kwargs):
        super(CityPickerWidget, self).__init__(*args, **kwargs)


    def render(self, name, value, attrs=None, renderer=None):
        if not renderer:
            renderer = get_default_renderer()
        context = self.get_context(name, value, attrs)
        if value:
            areaMsg = {0:"province", 1:"city", 2:"district", 3:"county"}
            areaData = value.split('/')
            cityPickerMsg = {areaMsg[i]:areaData[i] for i in range(len(areaData))}
            context.update({'cityPickerMsg':cityPickerMsg})
        return mark_safe(renderer.render('citypicker/citypicker.html', context))