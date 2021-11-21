from django import forms
from django.contrib.auth.models import User

from blog.models import Blog

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

    # method
    def clean_password2(self):
        cleaned = self.cleaned_data
        if cleaned['password'] != cleaned['password2']:
            raise forms.ValidationError('Password Dont Match')

        return cleaned['password2']

class BlogForms(forms.ModelForm):
    class Meta:
        model = Blog
        fields = ('title', 'content')

class BlogEditForms(forms.ModelForm):
    class Meta:
        model = Blog
        fields = ('title', 'content')