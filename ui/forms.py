from django import forms
from django.contrib.auth.forms import UserCreationForm
from users import models as user_models


class AddMaterialForm(forms.Form):
    material_name = forms.CharField(max_length=100, widget=forms.TextInput(
        attrs={
            "class": "form-control",
            "id": "material_name"
        }
    ))
    material_file = forms.FileField(widget=forms.FileInput(attrs={
        "class": "form-control",
        "id": "material_file"
    }))


class AddCourseForm(forms.Form):
    name = forms.CharField(max_length=100, widget=forms.TextInput(
        attrs={
            "class": "form-control",
            "id": "course_name"
        }
    ))

    description = forms.CharField(max_length=100, widget=forms.TextInput(
        attrs={
            "class": "form-control",
            "id": "course_description"
        }
    ))

    grade_level = forms.IntegerField(widget=forms.NumberInput(attrs={
        "class": "form-control",
        "id": "course_grade_level"

    }))
