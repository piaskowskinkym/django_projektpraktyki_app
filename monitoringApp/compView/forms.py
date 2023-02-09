from django import forms
from django.forms import ModelForm
from .models import ClassRoom,Computer

#Create
class ComputerForm(ModelForm):
    class Meta:
        model = Computer
        fields = "__all__"