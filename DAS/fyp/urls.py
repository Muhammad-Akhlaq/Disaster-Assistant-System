from django.contrib import admin
from django.urls import path,include
from fyp import views

urlpatterns = [
    path('', views.home, name='home'),
    path('Estimation_Earthquake/', views.Estimation_Earthquake, name='Estimation_Earthquake'),
    path('Estimation_Flood/', views.Estimation_Flood, name='Estimation_Flood'),
    path('news/', views.news, name='news'),
    path('events/<str:type>', views.events, name='events'),
    path('contact/', views.contact, name='contact'),
    path('weather/', views.weather, name='weather'),
    path('blogpost/<str:slug>', views.blogpost, name='blog'),
    path('blogupdate/<str:title>', views.blogupdate, name='blogupdate'),
    path('deleteblog/<str:title>', views.deleteblog, name='deleteblog'),
    path('awareness/', views.awareness, name='awareness'),
    path('search/', views.search, name='search'),
    path('bloghome/', views.blog, name='blog'),
    path('blogwrite/', views.blogwrite, name='blogwrite'),
    path('myblogs/<str:username>', views.myblogs, name='myblogs'),
    path('earthquake/', views.earthquake, name='earthquake'),
    path('flood/', views.flood, name='flood'),
    path('signup/', views.signup, name='signup'),
    path('myprofile/<str:username>', views.myprofile, name='myprofile'),
    path('login/', views.Login, name='login'),
    path('logout/', views.Logout, name='logout'),
    path('aboutus/', views.aboutus, name='aboutus')
]
