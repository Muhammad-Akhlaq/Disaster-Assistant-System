from django.contrib import admin
from django.urls import path,include
from fyp import views

urlpatterns = [
    path('', views.home, name='home'),
    path('estimation/', views.estimation, name='estimation'),
    path('news/', views.news, name='news'),
    path('events/', views.events, name='events'),
    path('contact/', views.contact, name='contact'),
    path('weather/', views.weather, name='weather'),
    path('blogpost/<str:slug>', views.blogpost, name='blog'),
    path('blogupdate/<str:title>', views.blogupdate, name='blogupdate'),
    path('awareness/', views.awareness, name='awareness'),
    path('search/', views.search, name='search'),
    path('bloghome/', views.blog, name='blog'),
    path('blogwrite/', views.blogwrite, name='blogwrite'),
    path('myblogs/', views.myblogs, name='myblogs'),
    path('earthquake/', views.earthquake, name='earthquake'),
    path('flood/', views.flood, name='flood'),
    path('signup/', views.signup, name='signup'),
    path('login/', views.Login, name='login'),
    path('logout/', views.Logout, name='logout')

]
