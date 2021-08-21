from django import forms
from .models import Task
from .choices import STATUS_CHOICE
from tinymce.models import HTMLField


class TaskCreateForm(forms.ModelForm):
    class Meta:
        model = Task
        fields = '__all__'


class TaskCreateCustomForm(forms.Form):
    name = forms.CharField(max_length=50)
    description = forms.CharField(widget=HTMLField)
    status = forms.ChoiceField(choices=STATUS_CHOICE)
