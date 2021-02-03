from django.shortcuts import render, HttpResponse
from fyp.models import Blog, Contact
import math


# Create your views here.

def home(request):

    return render(request, 'home.html')

def awareness(request):

    return render(request, 'awareness.html')

def estimation(request):

    return render(request, 'estimation.html')

def news(request):

    return render(request, 'news.html')

def events(request):

    return render(request, 'events.html')

def contact(request):

    return render(request, 'contact.html')

def blog(request):
    no_of_posts = 5
    page = (request.GET.get('page'))
    if page is None:
        page = 1
    else:
        page = int(page)
    blogs = Blog.objects.all()
    length = len(blogs)
    blogs = blogs[(page-1)*no_of_posts: page*no_of_posts]
    if page > 1:
        prev = page-1
    else:
        prev = None
    if page < math.ceil(length/no_of_posts):
        nxt = page + 1
    else:
        nxt = None
    context = {'blogs': blogs, 'prev': prev, 'nxt': nxt}
#    return HttpResponse("This is blog")
    return render(request, 'bloghome.html', context)


def blogpost(request, slug):
    blog = Blog.objects.filter(slug=slug).first
    context = {'blog': blog}
    return render(request, 'blogpost.html', context)


