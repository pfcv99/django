from django import forms
from .models import students
class studentsForm(forms.ModelForm):
    class Meta:
        model = students
        fields = ['id', 'gender', 'ageGroup', 'year', 'area']