from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from django.shortcuts import redirect, render
from django.views.generic import View
from blog.forms import *
from blog import models
# Create your views here.

def index(request):
    return render(request, 'index.html')


@login_required
def blog_homepage(request):
    photos = models.Photo.objects.all()
    return render(request, 'homepage.html', context={'photos': photos})

@login_required
def profile(request):
    return render(request, 'profile.html')

class upload_picture(View):
    form_class = PhotoForm
    template_name = 'blog/photo_upload.html'
    
    @method_decorator(login_required)
    def dispatch(self, *args, **kwargs):
        return super().dispatch(*args, **kwargs)

    def get(self, request):
        form = self.form_class()
        return render(request, self.template_name, context={'form':form})

    def post(self, request):
        form = self.form_class(request.POST, request.FILES)
        if (form.is_valid()):
            photo = form.save(commit=False)
            photo.uploader = request.user
            photo.save()
            return redirect('home')
        return render(request, 'photo_upload.html', context={'form':form})
