"""
URL configuration for core project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.contrib.auth.views import LoginView
from django.contrib.auth.views import LogoutView, PasswordChangeView, PasswordChangeDoneView
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
import authentication.views
import blog.views

urlpatterns = [
    path('admin/',
         admin.site.urls),
    
    path('',
         blog.views.index,
         name='index'),

    path('login/',
        LoginView.as_view(
            template_name='login.html',
            redirect_authenticated_user=True),
        name= 'login'),
    
    path('logout/', 
        LogoutView.as_view(), 
        name='logout'),

    path('signup', 
        authentication.views.signup_page.as_view(
             template_name='signup.html'),
        name='signup'),

    path('profil/password/change/', 
        PasswordChangeView.as_view(
            template_name='password_change.html',
            success_url='profil/password/change/success'), 
        name='pass_change'),
    
    path('profil/pp/change/', 
        authentication.views.change_picture.as_view(
            template_name='pp_change.html'), 
        name='pp_change'),
    
    path('profil/password/change/success', 
         PasswordChangeDoneView.as_view(
             template_name='password_change_success.html'), 
         name ='pass_change_success'),

    path('feed/',
         blog.views.blog_homepage,
         name='home'),
    
    path('feed/<int:blog_id>', 
        blog.views.view_blog, 
        name='view_blog'),

    path('feed/<int:blog_id>/edit',
        blog.views.edit_blog.as_view(
            template_name = 'edit_blog.html'),
        name = 'blog_edit'),

    path('feed/upload/post',
            blog.views.upload_post.as_view(
             template_name='blog_upload.html'),
         name='upload_post'),
    
    path('feed/upload/photo',
            blog.views.upload_picture.as_view(
             template_name='photo_upload.html'),
         name='upload_photo'),

    path('profil/',
         blog.views.profile,
         name= 'profile'),
]

if settings.DEBUG:
    urlpatterns += static(
        settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)