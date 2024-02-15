from django.shortcuts import render
from django.contrib.auth.decorators import login_required

# Create your views here.

@login_required
def blog_homepage(request):
	return render (request, 'blog_homepage.html')