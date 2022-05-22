from django.shortcuts import redirect, render
from django.contrib.auth.models import User,auth

# Create your views here.

def register(request):
     return render(request,'loginpage.html')
