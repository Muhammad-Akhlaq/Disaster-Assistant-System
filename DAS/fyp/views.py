from django.shortcuts import render, HttpResponse,redirect
from fyp.models import Blog, Contact
from django.contrib import messages
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.models import User
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



def weather(request):

    return render(request, 'weather.html')



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
        title= request.POST['title']
        content= request.POST['content']
        short_desc= request.POST['short_desc']
        slug= request.POST['slug']
        author= request.POST['author']        
        ins = Blog(title=title, content=content, short_desc=short_desc, slug=slug, author=author)
        ins.save()

        print('Data has been written in the database')
    return render(request, 'blogwrite.html')



def blogupdate(request, title):
    editblog = title
    blog = Blog.objects.filter(title=editblog).first
    context = {'blog':blog}
    if request.method=='POST':
        title= request.POST['title']
        content= request.POST['content']
        short_desc= request.POST['short_desc']
        slug= request.POST['slug']  
        Blog.objects.filter(title=editblog).update(title=title, content=content, short_desc=short_desc, slug=slug)

    return render(request, 'blogupdate.html',context)



def earthquake(request):

    return render(request, 'earthquake.html')



def flood(request):

    return render(request, 'flood.html')



def signup(request):
    if request.method=='POST':
        username= request.POST['username']
        fname= request.POST['fname']
        lname= request.POST['lname']
        email= request.POST['email']
        pass1= request.POST['pass1']
        pass2= request.POST['pass2']
        #checks
        if len(username) > 10 or len(username) < 5:
            messages.error(request,"Username must be under 5 to 10 characters")
            return redirect('/')
        if not username.isalnum():
            messages.error(request,"Username should only contain letters and numbers")
            return redirect('/')
        if pass1 != pass2:
            messages.error(request,"Passwords do not match")
        #create user
        myuser=User.objects.create_user(username,email,pass1)
        myuser.first_name=fname
        myuser.last_name=lname
        myuser.save() 
        messages.success(request,"Your Account is successfully created")
        return redirect("/")
    else:
        return HttpResponse("404-Not Found")



def Login(request):
    if request.method=='POST':
        loginusername= request.POST['loginusername']
        password= request.POST['pass']
        #authenticate
        user=authenticate(username=loginusername,password=password)
        if user is not None:
            login(request,user)
            messages.success(request,"Successfully logged in")
            return redirect("/")
        else:
            messages.error(request,"Invalid Credentials, Please try again")
            return redirect("/")
    else:
        return HttpResponse("404-Not Found")



def Logout(request):
    logout(request)
    messages.success(request,"Successfully logged out")
    return redirect("/")
    