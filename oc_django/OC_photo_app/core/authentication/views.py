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
        form = self.form_class(request.POST, request.FILES)
        if (form.is_valid()):
            user = form.save()
            login(request, user)
            return redirect('home')
        else:
            print(form.errors)
        return render(request, self.template_name, context={'form':form})

class change_picture(View):
    form_class = UpdatePP
    template_name = 'blog/pp_change.html'

    def get(self, request):
        form = self.form_class()
        return render(request, self.template_name, context={'form':form})
    def post(self, request):
        form = self.form_class(request.POST, request.FILES,instance=request.user)
        if (form.is_valid()):
            user = form.save()
            return redirect('profile')
        return render(request, self.template_name, context={'form':form})
    