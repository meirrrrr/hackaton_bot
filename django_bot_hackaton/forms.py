from django import forms

from .models import Teacher


class TeacherForm(forms.ModelForm):

    class Meta:
        model = Teacher
        fields = (
            'external_id',
            'first_name',
        )
        widgets = {
            'first_name': forms.TextInput,
        }
