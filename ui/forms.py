from django import forms
from django.contrib.auth.forms import UserCreationForm
from users import models as user_models
from session import models as session_models
from course import models as course_models


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


class school_admin_add_session_form(forms.ModelForm):
    def choice_parser(value):
        print(value)
        return course_models.Course.objects.get(id=value)

    course = forms.TypedChoiceField(coerce=choice_parser)

    class Meta:
        model = session_models.Session
        fields = ['course', 'description', 'start_time', 'end_time']

    def __init__(self, *args, **kwargs):
        super(school_admin_add_session_form, self).__init__(*args, **kwargs)
        self.fields['course'].choices = [(int(course.pk), course) for course in kwargs['initial']['courses']]
