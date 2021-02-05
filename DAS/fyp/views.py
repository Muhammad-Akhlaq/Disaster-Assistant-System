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
    if request.method=='POST':
        print('This is post')
        name= request.POST['name']
        email= request.POST['email']
        phone= request.POST['phone']
        desc= request.POST['desc']
        ins = Contact(name=name, email=email, phone=phone, desc=desc)
        ins.save()
        print('Data has been written in the database')
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

def search(request):
    query=request.GET['query']
    page=request.GET.get('page')
    print('page=',page)
    blogtitle=Blog.objects.filter(title__icontains=query)
    blogintro=Blog.objects.filter(short_desc__icontains=query)
    blogs=blogtitle.union(blogintro)
    no_of_posts=5
    if page is None:
        page=1
    else:
        page=int(page)
    length=len(blogs)
    blogs=blogs[(page-1)*no_of_posts:page*no_of_posts]
    if page>1:
        prev = page-1
    else:
        prev = None
    if page<math.ceil(length/no_of_posts):
        nxt = page + 1
    else:
        nxt = None
    context={'blogs':blogs,'query':query,'prev':prev,"nxt":nxt}
    return render(request,'search.html',context)

def blogwrite(request):
    if request.method=='POST':
        print('This is post')
        #sno= request.POST['sno']
        title= request.POST['title']
        content= request.POST['content']
        short_desc= request.POST['short_desc']
        slug= request.POST['slug']
        time= request.POST['time']
        author= request.POST['author']        
        ins = Blog(title=title, content=content, short_desc=short_desc, slug=slug, time=time, author=author)
        ins.save()

        print('Data has been written in the database')
    return render(request, 'blogwrite.html')