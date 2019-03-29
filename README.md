# django-citypicker
### 说明
django的model字段，结合citypicker的js插件，实现选择城市的功能
### 使用
- 在项目的settings.py中加入django-citypicker这个app
- 在models.py文件中导入
```python
  from django-citypickerimport CityPicker
  ```
- model中引用
```python
  class TestModel(model.Models):
    xxx = CityPicker()
```
