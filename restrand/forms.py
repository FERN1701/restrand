from django.forms import ModelForm
from django.contrib.auth.forms import UserCreationForm
from .models import *
from django import forms

class MyUserCreationForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['email', 'password1', 'password2']
        widgets = {
            'email':forms.EmailInput(attrs={'class':'form-control'}),
        }


class system_form(ModelForm):
    class Meta:
        model = setting_detail
        fields = ['details']
        widgets = {
            'details': forms.Textarea(attrs={'class': 'form-control'}),
}
        

class team_forms(ModelForm):
    class Meta:
        model = team_detail
        fields = ['team_image','team_name','team_description']
        widgets = {
            'team_image': forms.ClearableFileInput(attrs={'class': 'form-control'}),
            'team_name': forms.TextInput(attrs={'class': 'form-control'}),
            'team_description': forms.Textarea(attrs={'class': 'form-control', 'rows':'3'}),
}


