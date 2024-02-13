from django.shortcuts import redirect, render
from authentication.form import *
from django.contrib.auth import login, authenticate, logout
# Create your views here.

def login_page(request):
    form = loginForm()
    message = ''
    if (request.method == 'POST'):
        form = loginForm(request.POST)
        if (form.is_valid()):
            user = authenticate(
                username = form.cleaned_data['username'],
                password = form.cleaned_data['password'],
            )
            if (user is not None):
                login(request, user)
                message = f'Bonjour {user.username}, vous etes connecte'
            else:
                message = 'Invalid username/password'
    return render(request, 
                  'login.html',
                  context={'form':form,
                           'message': message})


def logout_user(request):
    logout(request)
    return redirect('login')