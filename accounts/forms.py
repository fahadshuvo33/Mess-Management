from django import forms
from accounts.models import CustomUser
from django.contrib.auth import get_user_model

class UserRegistrationForm(forms.Form):
    mess_name = forms.CharField(label="Mess Name", max_length=100)
    username = forms.CharField(label="Username", max_length=30)
    email = forms.EmailField(label="Email")
    phone = forms.CharField(label="Phone Number", max_length=15)
    password = forms.CharField(label="Password", widget=forms.PasswordInput)

    class Meta:
        model = CustomUser  
        fields = ['mess_name', 'username', 'email', 'phone', 'password']

