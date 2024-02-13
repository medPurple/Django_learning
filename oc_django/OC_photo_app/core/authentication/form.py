from django import forms


class loginForm(forms.Form):
    username = forms.CharField(max_length=63, label= 'Username')
    password = forms.CharField(max_length=62, 
                               widget=forms.PasswordInput, 
                               label= 'Password')