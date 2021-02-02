from django.contrib import admin
from django.urls import path,include
from fyp import views

urlpatterns = [
    path('', views.home, name='home'),
    path('awareness/', views.awareness, name='awareness'),
    path('estimation/', views.estimation, name='estimation'),
    path('news/', views.news, name='news'),
    path('events/', views.events, name='events'),
    path('contact/', views.contact, name='contact'),


]
