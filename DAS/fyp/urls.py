from django.contrib import admin
from django.urls import path,include
from fyp import views

urlpatterns = [
    path('', views.home, name='home'),
    path('estimation/', views.estimation, name='estimation'),
    path('news/', views.news, name='news'),
    path('events/', views.events, name='events'),
    path('contact/', views.contact, name='contact'),
    path('blogpost/<str:slug>', views.blogpost, name='blog'),
    path('awareness/', views.awareness, name='awareness'),
    path('blog/', views.blog, name='blog')
]
