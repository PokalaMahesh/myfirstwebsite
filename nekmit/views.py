from django.shortcuts import render
from . models import  business

def index(request):

    shop1 = business.objects.all()

    return render(request, 'index.html',{'shop' : shop1})

# Create your views here.
