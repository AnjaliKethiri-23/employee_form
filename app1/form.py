from django import forms
from app1.models import student
class new_employee(forms.ModelForm):
    class Meta:
        fields="__all__"
        model=student