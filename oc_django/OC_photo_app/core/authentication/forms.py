from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import get_user_model
from django import forms

class SignupForm(UserCreationForm):
    profile_pic = forms.ImageField(label='Profile Picture')
    class Meta(UserCreationForm.Meta):
        model = get_user_model()
        fields = (
            'username',
            'first_name', 
            'last_name', 
            'email',
            'role',
            'profile_pic'
        )
