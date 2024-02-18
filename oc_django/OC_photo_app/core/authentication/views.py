from django.shortcuts import redirect, render
from authentication.forms import *
from django.contrib.auth import login, authenticate, logout
from django.views.generic import View
from django.conf import settings
# Create your views here.

class signup_page(View):
    form_class = SignupForm
    template_name = 'authentication/signup.html'
    
    def get(self, request):
        form = self.form_class()
        return render(request, self.template_name, context={'form':form})
    def post(self, request):
        form = self.form_class(request.POST)
        if (form.is_valid()):
            user = form.save()
            login(request, user)
            return redirect('home')
        return render(request, self.template_name, context={'form':form})