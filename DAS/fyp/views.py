from django.shortcuts import render, HttpResponse,redirect, get_object_or_404
from fyp.models import Blog, Contact
from django.contrib import messages
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.models import User
import math
import json 
import urllib.request
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsClassifier
# Create your views here.

def home(request):

    return render(request, 'home.html')



def awareness(request):

    return render(request, 'awareness.html')



def estimation(request):
    context={}
    if request.method=='POST':
        print('This is post')
        severity= request.POST['Severity']
        affected= request.POST['Affected Area']
        magnitude= request.POST['Magnitude']
        c_x= request.POST['Centroid X']
        c_y= request.POST['Centroid Y']
        data = pd.read_excel('static/c.xls')
        data.dropna(inplace=True)
        X = data.drop(['Dead','Nothing','Displaced','Duration in Days'],axis=1)
        y = data['Dead']
        X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=101)
        knn = KNeighborsClassifier(n_neighbors=25)
        knn.fit(X_train,y_train)
        pred = knn.predict([[severity,affected,magnitude,c_x,c_y]])
        context={'pred':pred}
    return render(request, 'estimation.html',context)



def news(request):

    return render(request, 'news.html')



def events(request):

    return render(request, 'events.html')



def weather(request):
    if request.method == 'POST': 
        city = request.POST['city'] 
        ''' api key might be expired use your own api_key 
            place api_key in place of appid ="your_api_key_here "  '''
  
        # source contain JSON data from API 
  
        source = urllib.request.urlopen( 
            'http://api.openweathermap.org/data/2.5/weather?q='+ city +'&appid=f0b7bbd617bd589d478db5cfb6a08685').read() 
  
        # converting JSON data to a dictionary 
        list_of_data = json.loads(source) 
  
        # data for variable list_of_data 
        data = { 
            "country_code": str(list_of_data['sys']['country']), 
            "coordinate": str(list_of_data['coord']['lon']) + ' '
                        + str(list_of_data['coord']['lat']), 
            "temp": str(list_of_data['main']['temp']) + 'k', 
            "pressure": str(list_of_data['main']['pressure']), 
            "humidity": str(list_of_data['main']['humidity']),
            "Description": str(list_of_data['weather'][0]['description']),
        } 
        print(data) 
    else: 
        data ={}

    return render(request, 'weather.html',data)



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
    context={}
    if request.method=='POST':
        title= request.POST['title']
        content= request.POST['content']
        short_desc= request.POST['short_desc']
        slug= request.POST['slug']
        author= request.POST['author']
        username= request.POST['username']
        context={'title':title,'short_desc':short_desc,'slug':slug,'author':author}
        if content!='':        
            ins = Blog(title=title, content=content, short_desc=short_desc, slug=slug, author=author,username=username)
            ins.save()
            messages.error(request,"Blog successfully written!")
            context={}
            return redirect('/bloghome')

        else:
            messages.error(request,"Content is blanked...Write something")
    return render(request, 'blogwrite.html',context)



def myblogs(request,username):
    blogs = Blog.objects.filter(username=username)
    context={'blogs':blogs}
    

    return render(request, 'myblogs.html',context)



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
        messages.error(request,"Blog successfully Updated!")
        return redirect('/bloghome/')
    return render(request, 'blogupdate.html',context)



#def deleteblog(request, title):
 #   editblog = title
  #  blog = Blog.objects.filter(title=editblog).first
   # context = {'blog':blog}
    #if request.method=='POST':
     #   obj.delete()


      #  messages.error(request,"Blog successfully Updated!")
       # return redirect('/bloghome/')
    #return render(request, 'deleteblog.html',context)


def deleteblog(request,title):
    editblog = title
    obj=get_object_or_404(Blog,title=editblog)
    if request.method == "POST":
        obj.delete()
        return redirect("/bloghome")
    return render(request,"deleteblog.html",{"obj":obj})


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
            return redirect("/awareness")
        else:
            messages.error(request,"Invalid Credentials, Please try again")
            return redirect("/")
    else:
        return HttpResponse("404-Not Found")



def Logout(request):
    logout(request)
    messages.success(request,"Successfully logged out")
    return redirect("/")
    