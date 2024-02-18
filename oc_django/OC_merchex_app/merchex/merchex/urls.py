"""
URL configuration for merchex project.

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
from django.urls import path
from listings import views

urlpatterns = [
    path('admin/', admin.site.urls),
<<<<<<< HEAD
    path('index', views.index, name='index'),
=======
    path('index/', views.index, name='index'),
>>>>>>> refs/remotes/origin/main
    path('about/', views.about, name='about'),
    path('contact/', views.contact, name='contact'),
    
    path('bands/', views.band_list, name='band-list'),
    path('bands/<int:band_id>/',views.band_detail, name='band_detail'),
    path('band/add/', views.band_create, name='band_create'),
    path('email_success/', views.email_success, name='email_sent'),
    path('bands/<int:band_id>/change/', views.update_band, name='band_update'),
    path('bands/<int:band_id>/delete/', views.delete_band, name='band_delete'),
    
    path('lists/', views.listings_list, name='list-list'),
    path('lists/<int:list_id>/',views.listings_detail, name='lists_detail'),
    path('lists/<int:list_id>/change/', views.update_lists, name='lists_update'),
    path('lists/<int:list_id>/delete/', views.delete_lists, name='lists_delete'),
    path('lists/add/', views.lists_create, name='lists_create'),
    
]
