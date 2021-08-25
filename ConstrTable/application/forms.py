from django import forms
from .models import Application
import re
from django.core.exceptions import ValidationError


class ApplicationForm(forms.ModelForm):
    class Meta:
        model = Application
        fields = ['name', 'brand', 'quantity', 'link', 'item', 'shop', 'area']
        widgets = {
            'name': forms.TextInput(attrs={"class": "form-control"}),
            'brand': forms.TextInput(attrs={"class": "form-control"}),
            'quantity': forms.NumberInput(attrs={"class": "form-control"}),
            'link': forms.URLInput(attrs={"class": "form-control"}),
            'item': forms.NumberInput(attrs={"class": "form-control"}),
            'shop': forms.TextInput(attrs={"class": "form-control"}),
            'area': forms.Select(attrs={"class": "form-control"}),

        }

    #кастомный валидатор Наименования
    def clean_name(self):
        name = self.cleaned_data['name']
        if re.match(r'\d', name):
            raise ValidationError('Название не должно начинаться с цифры')
        return name
    #Нужно будет написать еще валидаторы для полей