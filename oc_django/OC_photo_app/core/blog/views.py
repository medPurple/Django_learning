from django.contrib.auth.decorators import login_required
from django.shortcuts import get_object_or_404
from django.utils.decorators import method_decorator
from django.shortcuts import redirect, render
from django.views.generic import View
from django.forms import formset_factory
from blog.forms import *
from blog import models
# Create your views here.

def index(request):
    return render(request, 'index.html')


@login_required
def blog_homepage(request):
    photos = models.Photo.objects.all()
    blogs = models.Blog.objects.all()
    return render(request, 'homepage.html', context={'photos': photos, 'blogs':blogs})

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

class upload_post(View):
    pform_class = PhotoForm
    bform_class = BlogForm
    template_name = 'blog_upload.html'
    
    @method_decorator(login_required)
    def dispatch(self, *args, **kwargs):
        return super().dispatch(*args, **kwargs)

    def get(self, request):
        pform = self.pform_class()
        bform = self.bform_class()
        return render(request, self.template_name, context={'blog_form':bform, 'photo_form':pform})

    def post(self, request):
        pform = self.pform_class(request.POST, request.FILES)
        bform = self.bform_class(request.POST)
        if all([bform.is_valid(), pform.is_valid()]):
            photo = pform.save(commit=False)
            photo.uploader = request.user
            photo.save()
            blog = bform.save(commit=False)
            blog.author = request.user
            blog.photo = photo
            blog.save()
            return redirect('home')
        return render(request, self.template_name,  context={'blog_form':bform, 'photo_form':pform})

@login_required
def view_blog(request, blog_id):
    blog = get_object_or_404(models.Blog, id=blog_id)
    return render(request, 'view_blog.html', {'blog': blog})

class edit_blog(View):
    template_name = 'edit_blog.html'
    bform = BlogForm
    dform = DeleteBlogForm


    @method_decorator(login_required)
    def dispatch(self, *args, **kwargs):
        return super().dispatch(*args, **kwargs)

    def get(self, request, blog_id):
        blog = get_object_or_404(models.Blog, id=blog_id)
        edit_form = self.bform(instance=blog)
        delete_form = self.dform()
        context = {
            'edit_form': edit_form,
            'delete_form': delete_form,
        }
        return render(request, self.template_name, context=context)

    def post(self, request, blog_id):
        blog = get_object_or_404(models.Blog, id=blog_id)
        edit_form = self.bform(request.POST)
        delete_form = self.dform(request.POST)

        if (edit_form in request.POST):
            if (edit_form.is_valid()):
                edit_form.save()
                return (redirect('home'))
        if (delete_form in request.POST):
            if (delete_form.is_valid()):
                blog.delete
                return redirect('home')
        context={
            'edit_form': edit_form,
            'delete_form': delete_form,
        }
        return render (request, self.template_name, context=context)


