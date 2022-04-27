from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
    path('joinmeet', views.joinmeet, name='joinmeet'),
    path('homepage', views.homepage, name='homepage'),
    path('coursePage', views.coursePage, name='coursePage'),
]
