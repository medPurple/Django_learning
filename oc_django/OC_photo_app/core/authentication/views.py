from django.shortcuts import redirect, render
from authentication.forms import *
from django.contrib.auth import login, authenticate, logout
from django.views.generic import View

# Create your views here.