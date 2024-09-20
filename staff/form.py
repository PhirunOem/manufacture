from django.contrib.auth.forms import UserCreationForm, AuthenticationForm, PasswordChangeForm, UserChangeForm
from django.contrib.auth import password_validation
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, ButtonHolder, Submit, Fieldset,Row,Field
# from .models import staffInfo, User
from django.forms import ModelForm
from django import forms
from django.contrib.auth.models import User
from django.utils.translation import gettext, gettext_lazy as _
'''Note that : all form we use built-in form in django. for next development we should learn how to add more field like avarta etc.'''
#sign up account form 
class RegistrationForm(UserCreationForm):
    def __init__(self, *args, **kwargs):
        super(RegistrationForm, self).__init__(*args, **kwargs)
        self.fields['username'].label = "Your full name:"
        for fieldname in ['username', 'password1', 'password2']:
            self.fields[fieldname].help_text = None
        self.fields['username'].label = "Your full name:"
    class Meta:
        model = User
        fields = ['username','password1', 'password2']

#sign in account form       
class UserLoginForm(AuthenticationForm):
    def __init__(self, *args, **kwargs):
        super(UserLoginForm, self).__init__(*args, **kwargs)
    username = forms.CharField(widget=forms.TextInput())
    password = forms.CharField(widget=forms.PasswordInput())

#user change password form. use to handle user change password action
class UserChangePasswordForm(PasswordChangeForm):
    old_password = forms.CharField( required=True ,widget=forms.PasswordInput({"placeholder": "Your old password"}), label='')
    new_password1 = forms.CharField(required=True,widget=forms.PasswordInput({"placeholder": "Your new password"}), label='')
    new_password2 = forms.CharField(required=True,widget=forms.PasswordInput({"placeholder": "Re-enter old password"}), label='')
    def __init__(self, *args, **kwargs):
        super(UserChangePasswordForm, self).__init__(*args, **kwargs)
        for fieldname in ['old_password', 'new_password1', 'new_password2']:
            self.fields[fieldname].help_text = None

#user edit their profile form like their name or email          
class UserEditProfileForm(ModelForm):
    username = forms.CharField( required=True ,widget=forms.TextInput({"placeholder": "Your new name"}), label='')
    class Meta:
        model = User
        fields = ['username']
        