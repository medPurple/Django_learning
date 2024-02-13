from django.db import models
from django.contrib.auth.models import AbstractUser
# Create your models here.


class User(AbstractUser):
    CREATOR = 'CREATOR'
    SUBSCRIBER = 'SUBSCRIBER'
    
    ROLE_CHOICE = (
        (CREATOR, 'Creator'),
        (SUBSCRIBER, 'Subscriber'),
    )
    profile_pic = models.ImageField(verbose_name='Profile Picture')
    role = models.CharField(max_length=30, choices=ROLE_CHOICE, verbose_name='Role')
    