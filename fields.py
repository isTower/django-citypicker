#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Time    : 2019/3/29 17:40
# @Author  : Money
# @Site    : 
# @File    : fields.py
# @Software: PyCharm

from django import forms
from django.db import models

from .widgets import CityPickerWidget




class CityPickerField(models.TextField):

    def __init__(self, *args, **kwargs):
        self.config_name = kwargs.pop("config_name", "default")
        super(CityPickerField, self).__init__(*args, **kwargs)

    def formfield(self, **kwargs):
        defaults = {
            'form_class': self._get_form_class(),
            'config_name': self.config_name,
        }
        defaults.update(kwargs)
        return super(CityPickerField, self).formfield(**defaults)

    @staticmethod
    def _get_form_class():
        return CityPickerFormField


class CityPickerFormField(forms.fields.CharField):

    def __init__(self, config_name='default',  *args, **kwargs):
        kwargs.update({'widget': CityPickerWidget(config_name=config_name)})
        super(CityPickerFormField, self).__init__(*args, **kwargs)