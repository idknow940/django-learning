from django import forms
from .models import Profile


class UserLoginForm(forms.Form):
    username = forms.CharField(max_length=50)
    password = forms.CharField(widget=forms.PasswordInput)


class CreateProfile(forms.ModelForm):
    class Meta:
        model = Profile
        fields = '__all__'
        exclude = ('user', )
