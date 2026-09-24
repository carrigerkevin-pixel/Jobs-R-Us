from django.contrib.auth.forms import UserCreationForm
from .models import User
from .models import ApplicantProfile
from django.forms import ModelForm

class CustomUserCreationForm(UserCreationForm):
    class Meta: 
        model = User
        fields = [
            "username",
            "userType",
            "password1",
            "password2",
        ]

class ProfileEditForm(ModelForm):
    class Meta:
        model = ApplicantProfile
        exclude = ['user']