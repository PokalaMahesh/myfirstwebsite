from django.urls import path

from accounts import urls

from . import views

urlpatterns = [
    path('',views.index, name='index')
]