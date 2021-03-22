from django.contrib import admin
from django.urls import path,include
from fyp import views

urlpatterns = [
    path('', views.home, name='home'),
    path('Earthquake_Deaths/', views.Earthquake_Deaths, name='Earthquake_Deaths'),
    path('Earthquake_Injured/', views.Earthquake_Injured, name='Earthquake_Injured'),
    path('Earthquake_Affected/', views.Earthquake_Affected, name='Earthquake_Affected'),
    path('Flood_Deaths/', views.Flood_Deaths, name='Flood_Deaths'),
    path('Flood_Displaced/', views.Flood_Displaced, name='Flood_Displaced'),
    path('news/', views.news, name='news'),
    path('Flood_Events/<str:type>', views.Flood_Events, name='Flood_Events'),
    path('Earthquake_Events/<str:type>', views.Earthquake_Events, name='Earthquake_Events'),
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
    path('CovidLive/', views.CovidLive, name='CovidLive'),
    path('help/', views.help, name='help'),
    path('live/', views.live, name='live'),
    path('newmap/', views.newmap, name='newmap'),
    path('aboutus/', views.aboutus, name='aboutus')
]
