from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
#from phonenumber_field.modelfields import PhoneNumberField
from django.forms.utils import ValidationError
class UserRegistrationForm(UserCreationForm):
    email=forms.EmailField(max_length=200,help_text='Required,Please enter a valid email address')

    class Meta:
        model=User
        fields=('username','email','password1','password2',)

    def clean_email(self):
        email=self.cleaned_data['email']
        if User.objects.filter(email=email).exists():
            raise ValidationError('Email already registered! please enter another email')
        return email
