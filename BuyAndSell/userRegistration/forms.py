from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import UserPersonalInfo,NewBook
from django.forms import ModelForm


class RegisterForm(UserCreationForm):
    email = forms.EmailField()

    class Meta:
        model = User
        fields=['username','first_name','last_name','email','password1','password2']


class UserInfoForm(ModelForm):
    class Meta:
        model= UserPersonalInfo
        # fields=['BookName','Price','Year','Tag1','Tag2','BookImage']
        fields=['PhoneNo','City','Institute','SubUrb']
            
        


class UserNewBook(ModelForm):
    class Meta:
        model = NewBook
        fields=['BookName','Price','Year','Tag1','Tag2','BookImage']
        labels = {
            'year':"Book's Academic Year ?",
            'branch': "Book's Branch ?"         
            }   