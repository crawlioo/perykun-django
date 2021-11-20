from django import forms
from django.contrib.auth.models import User

class LoginForm(forms.Form):
    username = forms.CharField(max_length=255)
    password = forms.CharField(widget=forms.PasswordInput)

# registration forms
class RegisterForm(forms.ModelForm):
    password = forms.CharField(label='Password', widget=forms.PasswordInput)
    password2 = forms.CharField(label='confirm Password', widget=forms.PasswordInput)


    class Meta:
        model = User
        fields = ('username', 'first_name', 'email')

