from django.shortcuts import render, HttpResponse,redirect, get_object_or_404,HttpResponseRedirect,reverse
from fyp.models import Blog, Contact, E_Awareness,F_Awareness, UserProfile
from django.contrib import messages
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.models import User
import math
import json, requests
import urllib.request
import pandas as pd
from django.contrib.auth import update_session_auth_hash
from django.core.files.storage import FileSystemStorage
# Create your views here.

def home(request):

    return render(request, 'home.html')


def help(request):

    return render(request, 'help.html')


def live(request):

    return render(request, 'live.html')


def CovidLive(request):

    return render(request, 'CovidLive.html')

def newmap(request):
    earthquake = pd.read_excel("static/Earthquake.xlsx")
    positions = []
    country = earthquake['Country']
    lat = earthquake['Latitude']
    longi = earthquake['Longitude']
    for i in range(0,len(country)):
        a=[country[i],float(lat[i]),float(longi[i])]
        positions.append(a)
    context={'positions':positions}
    return render(request,'newmap.html',context)


def awareness(request):

    return render(request, 'awareness.html')


def Earthquake_Deaths(request):
    context={}
    Type=0
    Asia=0
    Africa=0
    Americas=0
    Europe=0
    Oceania=0
    if request.method=='POST':
        print('This is post')
        Earthquake_Type= request.POST['Earthquake_Type']
        Continent= request.POST['Continent']
        Magnitude= request.POST['Magnitude']
        Latitude= request.POST['Latitude']
        Longitude= request.POST['Longitude']
        if Earthquake_Type=='Ground_Movement':
            Type=1
        if Continent=='Africa':
            Africa=1
        elif Continent=='Asia':
            Asia=1
        elif Continent=='Americas':
            Americas=1
        elif Continent=='Europe':
            Europe=1
        else:
            Oceania=1
        print(Continent)
        Dead = Earthquake_Dead_Predictions(Type, Africa, Americas, Asia, Europe, Oceania, Magnitude, Latitude, Longitude)
        context={'Dead':Dead,'Display':None}
    return render(request, 'Earthquake_Deaths.html',context)


def Earthquake_Injured(request):
    context={}
    Type=0
    Asia=0
    Africa=0
    Americas=0
    Europe=0
    Oceania=0
    if request.method=='POST':
        print('This is post')
        Earthquake_Type= request.POST['Earthquake_Type']
        Continent= request.POST['Continent']
        Magnitude= request.POST['Magnitude']
        Latitude= request.POST['Latitude']
        Longitude= request.POST['Longitude']
        if Earthquake_Type=='Ground_Movement':
            Type=1
        if Continent=='Africa':
            Africa=1
        elif Continent=='Asia':
            Asia=1
        elif Continent=='Americas':
            Americas=1
        elif Continent=='Europe':
            Europe=1
        else:
            Oceania=1
        print(Continent)
        Injured = Earthquake_Injured_Predictions(Type, Africa, Americas, Asia, Europe, Oceania, Magnitude, Latitude, Longitude)
        context={'Injured':Injured,'Display':None}
    return render(request, 'Earthquake_Injured.html',context)

def Earthquake_Affected(request):
    context={}
    Type=0
    Asia=0
    Africa=0
    Americas=0
    Europe=0
    Oceania=0
    if request.method=='POST':
        print('This is post')
        Earthquake_Type= request.POST['Earthquake_Type']
        Continent= request.POST['Continent']
        Magnitude= request.POST['Magnitude']
        Latitude= request.POST['Latitude']
        Longitude= request.POST['Longitude']
        if Earthquake_Type=='Ground_Movement':
            Type=1
        if Continent=='Africa':
            Africa=1
        elif Continent=='Asia':
            Asia=1
        elif Continent=='Americas':
            Americas=1
        elif Continent=='Europe':
            Europe=1
        else:
            Oceania=1
        print(Continent)
        Affected = Earthquake_Affected_Predictions(Magnitude, Latitude, Longitude)
        context={'Affected':Affected,'Display':None}
    return render(request, 'Earthquake_Affected.html',context)


import pickle
def Earthquake_Dead_Predictions(Type, Africa, Americas, Asia, Europe, Oceania, Magnitude, Latitude, Longitude):
    model = pickle.load(open('Earthquake_Dead_RF.sav', 'rb'))

    prediction = model.predict([
        [Type, Africa, Americas, Asia, Europe, Oceania, Magnitude, Latitude, Longitude]
    ])
    return prediction
def Earthquake_Injured_Predictions(Type, Africa, Americas, Asia, Europe, Oceania, Magnitude, Latitude, Longitude):
    model = pickle.load(open('Earthquake_Injured_RF.sav', 'rb'))

    prediction = model.predict([
        [Type, Africa, Americas, Asia, Europe, Oceania, Magnitude, Latitude, Longitude]
    ])
    return prediction
def Earthquake_Affected_Predictions(Magnitude, Latitude, Longitude):
    model = pickle.load(open('Earthquake_Affected_RF.sav', 'rb'))

    prediction = model.predict([
        [Magnitude, Latitude, Longitude]
    ])
    return prediction


def Flood_Deaths(request):
    context={}
    if request.method=='POST':
        print('This is post')
        severity= request.POST['Severity']
        affected= request.POST['Affected Area']
        magnitude= request.POST['Magnitude']
        c_x= request.POST['Centroid X']
        c_y= request.POST['Centroid Y']
        Dead = Flood_Dead_Predictions(severity,affected,magnitude,c_x,c_y)
        context={'Dead':Dead,'Display':None}
    return render(request, 'Flood_Deaths.html',context)

def Flood_Displaced(request):
    context={}
    if request.method=='POST':
        print('This is post')
        severity= request.POST['Severity']
        affected= request.POST['Affected Area']
        magnitude= request.POST['Magnitude']
        c_x= request.POST['Centroid X']
        c_y= request.POST['Centroid Y']
        Displaced = Flood_Displaced_Predictions(severity,affected,magnitude,c_x,c_y)
        context={'Displaced':Displaced,'Display':None}
    return render(request, 'Flood_Displaced.html',context)

def Flood_Dead_Predictions(severity,affected,magnitude,c_x,c_y):
    model = pickle.load(open('Flood_Dead_RF.sav', 'rb'))

    prediction = model.predict([
        [severity,affected,magnitude,c_x,c_y]
    ])
    return prediction
def Flood_Displaced_Predictions(severity,affected,magnitude,c_x,c_y):
    model = pickle.load(open('Flood_Displaced_RF.sav', 'rb'))

    prediction = model.predict([
        [severity,affected,magnitude,c_x,c_y]
    ])
    return prediction



import itertools
def news(request):
    '''
    response = requests.get(url = "https://api.reliefweb.int/v1/reports?appname=apidoc&limit=10")
    news = response.json()
    titles=[]
    body=[]
    country=[]
    date=[]
    for i in range(0,10):
        titles.append(str(news['data'][i]['fields']['title']))
        detail=news['data'][i]['href']
        response = requests.get(url = detail)
        new_detail = response.json()
        body.append(new_detail['data'][0]['fields']['body-html'])
        country.append(new_detail['data'][0]['fields']['country'][0]['name'])
        date.append(str(new_detail['data'][0]['fields']['date']['created']))
    data = itertools.zip_longest(body,titles, country, date)
    context = {'data':data}
    return render(request, 'news.html',context)'''
    """
    response = requests.get(url = "https://earthquake.usgs.gov/fdsnws/event/1/query?format=geojson&starttime=2020-01-01&endtime=2021-01-02&minmagnitude=4"
)
    data = response.json()
    titles=[]
    place=[]
    time=[]
    mag=[]
    coordinates=[]
    url=[]
    alert=[]
    magType=[]
    for i in range(0,10):
        titles.append(data['features'][i]['properties']['title'])
        place.append(data['features'][i]['properties']['place'])
        time.append(data['features'][i]['properties']['time'])
        mag.append(data['features'][i]['properties']['mag'])
        coordinates.append(data['features'][i]['geometry']['coordinates'])
        url.append(data['features'][i]['properties']['url'])
        alert.append(data['features'][i]['properties']['alert'])
        magType.append(data['features'][i]['properties']['magType'])



    data = itertools.zip_longest(titles, place,time,mag,coordinates,url,alert,magType)
    """
    page = (request.GET.get('page'))
    prev = 0
    if page is None:
        page = 1
    else:
        page = int(page)
    next = str((page-1)*5)
    response = requests.get(url = "https://api.reliefweb.int/v1/disasters?appname=rwint-user-0&offset="+next+"&profile=full&preset=latest&slim=1")
    news = response.json()
    headline=[]
    discription=[]
    country=[]
    date=[]
    type=[]
    status=[]
    for i in range(0,5):
        headline.append(str(news['data'][i]['fields']['name']))
        discription.append(news['data'][i]['fields']['description-html'])
        country.append(news['data'][i]['fields']['country'][0]['name'])
        date.append(str(news['data'][i]['fields']['date']['created']))
        type.append(str(news['data'][i]['fields']['type'][0]['name']))
        status.append(str(news['data'][i]['fields']['status']))
    data = itertools.zip_longest(headline,discription, country, date,type,status)
    next = page+1
    if page>=1:
        prev = page-1
    else:
        page=None
    context = {'data':data, 'prev': prev, 'next': next}
    return render(request, 'news.html',context)




def Flood_Events(request,type):
    Flood_no = []
    year_lebel = []
    Flood = pd.read_csv("static/Flood.csv")
    count = Flood['Year'].value_counts()
    count = count.sort_index()
    for i in count:
        Flood_no.append(i)
    for j in count.index:
        year_lebel.append(j)
    deaths,deaths_years,dead_count,dead_label = deathgraph(Flood['Dead'],Flood['Year'],Flood['Death'])
    print(dead_count)
    print(dead_label)
    Displaced,Displaced_years,Displaced_count,Displaced_label = Injuredgraph(Flood['Displaced'],Flood['Year'],Flood['Displace'])
    context = {'display2':'none','display':'block'}
    if type=='visual':
        context = {'display2':'block','display':'none','data':Flood_no,'lebel':year_lebel,'deaths':deaths,'deaths_years':deaths_years,'dead_count':dead_count,'dead_label':dead_label,
        'Displaced':Displaced,'Displaced_years':Displaced_years,'Displaced_label':Displaced_label,'Displaced_count':Displaced_count}
    return render(request, 'Flood_Events.html',context)









def Earthquake_Events(request,type):
    earthquake_no = []
    year_lebel = []
    earthquake = pd.read_excel("static/Earthquake.xlsx")
    count = earthquake['Year'].value_counts()
    country = earthquake['Country'].unique()
    country.sort()
    count = count.sort_index()
    for i in count:
        earthquake_no.append(i)
    for j in count.index:
        year_lebel.append(j)
    deaths,deaths_years,dead_count,dead_label = deathgraph(earthquake['Total Deaths'],earthquake['Year'],earthquake['Dead'])
    print(dead_count)
    print(dead_label)
    Injured,Injured_years,Injured_count,Injured_label = Injuredgraph(earthquake['No Injured'],earthquake['Year'],earthquake['Injured'])
    Affected,Affected_years,Affected_count,Affected_label = Affectedgraph(earthquake['Total Affected'],earthquake['Year'],earthquake['Affected'])
    context = {'display2':'none','display':'block'}
    if type=='visual':
        context = {'display2':'block','display':'none','Country':country,'data':earthquake_no,'lebel':year_lebel,'deaths':deaths,'deaths_years':deaths_years,'dead_count':dead_count,'dead_label':dead_label,
        'Injured':Injured,'Injured_years':Injured_years,'Injured_label':Injured_label,'Injured_count':Injured_count,'Affected':Affected,'Affected_years':Affected_years,
        'Affected_count':Affected_count,'Affected_label':Affected_label}
    return render(request, 'Earthquake_Events.html',context)
def deathgraph(dead,year,dead_label):
    deaths = []
    years = []
    label = []
    label_count = []
    dead_label = dead_label.value_counts()
    for i in dead_label:
        label_count.append(i)
    for i in dead_label.index:
        label.append(i)
    index = dead[dead>100000].index
    year = year.drop(index,axis=0)
    dead = dead[dead<100000]
    for j in dead:
        deaths.append(j)
    for j in year:
        years.append(j)
    return deaths,years,label_count,label
def Injuredgraph(injureds,year,Injured_label):
    injured = []
    years = []
    label = []
    label_count = []
    Injured_label = Injured_label.value_counts()
    for i in Injured_label:
        label_count.append(i)
    for i in Injured_label.index:
        label.append(i)
    index = injureds[injureds>100000].index
    year = year.drop(index,axis=0)
    injureds = injureds[injureds<100000]
    for j in injureds:
        injured.append(j)
    for j in year:
        years.append(j)
    return injured,years,label_count,label
def Affectedgraph(Affecteds,year,Affected_label):
    Affected = []
    years = []
    label = []
    label_count = []
    Affected_label = Affected_label.value_counts()
    for i in Affected_label:
        label_count.append(i)
    for i in Affected_label.index:
        label.append(i)
    index = Affecteds[Affecteds>100000].index
    year = year.drop(index,axis=0)
    Affecteds = Affecteds[Affecteds<100000]
    for j in Affecteds:
        Affected.append(j)
    for j in year:
        years.append(j)
    return Affected,years,label_count,label




def weather(request):
    if request.method == 'POST': 
        city = request.POST['city'] 
        """
        source = urllib.request.urlopen( 
            'http://api.openweathermap.org/data/2.5/weather?q='+ city +'&appid=f0b7bbd617bd589d478db5cfb6a08685').read() 
   
        list_of_data = json.loads(source) 
  
        data = { 
            "country_code": str(list_of_data['sys']['country']), 
            "coordinate": str(list_of_data['coord']['lon']) + ' '
                        + str(list_of_data['coord']['lat']), 
            "temp": str(list_of_data['main']['temp']) + 'k', 
            "pressure": str(list_of_data['main']['pressure']), 
            "humidity": str(list_of_data['main']['humidity']),
            "Description": str(list_of_data['weather'][0]['description']),
        }
        """ 
        url = "http://api.worldweatheronline.com/premium/v1/weather.ashx?key=6c562dc1286349aeb43143853211303&q="+ city +"&mca=no&fx=no&num_of_days=2&alerts=yes&format=json"
        response = requests.request("GET", url)
        weather = response.json()
        try:
            alert = weather['data']['alerts']['alert'][0]['headline']
        except:
            alert = "No Alert"
        data = { 
            "location": str(weather['data']['request'][0]['query']), 
            "time": str(weather['data']['current_condition'][0]['observation_time']), 
            "temp": str(weather['data']['current_condition'][0]['temp_C']) + '°C', 
            "condition": str(weather['data']['current_condition'][0]['weatherDesc'][0]['value']), 
            "humidity": str(weather['data']['current_condition'][0]['humidity']),
            "icon": str(weather['data']['current_condition'][0]['weatherIconUrl'][0]['value']),
            "alert": alert
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
    user = User.objects.get(username=blog().username)
    context = {'blog': blog,'user_detail':user}
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
        Slug= request.POST['slug']
        author= request.POST['author']
        username= request.POST['username']
        context={'title':title,'short_desc':short_desc,'slug':Slug,'author':author,'content':content}
        check=""
        try:
            slug_ = Blog.objects.filter(slug=Slug).first
            check = slug_().slug
        except:
            check = ""
        print(check)
        if content=='':
           messages.error(request,"Content is blanked...Write something")
        elif check==Slug:
           messages.error(request,"Slug should be unique...Write again")
        else:
            ins = Blog(title=title, content=content, short_desc=short_desc, slug=Slug, author=author,username=username)
            ins.save()
            messages.error(request,"Blog successfully written!")
            context={}
            return redirect('/bloghome')
    return render(request, 'blogwrite.html',context)



def myblogs(request,username):
    blogs = Blog.objects.filter(username=username)
    print(blogs)
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



def deleteblog(request,title):
    editblog = title
    obj=get_object_or_404(Blog,title=editblog)
    if request.method == "POST":
        obj.delete()
        messages.error(request,"Blog successfully deleted!")
        return redirect("/bloghome")
    return render(request,"deleteblog.html",{"obj":obj})


def earthquake(request):

    awareness = E_Awareness.objects.filter().first
    context = {'awareness': awareness}

    return render(request, 'earthquake.html', context)



def flood(request):

    fawareness = F_Awareness.objects.filter().first
    context = {'fawareness': fawareness}

    return render(request, 'flood.html', context)



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
    return render(request,'signup.html')



def myprofile(request,username):
    user = User.objects.get(username=username)
    try:
        profile = UserProfile.objects.get(user=user.id)
    except:
        profile = UserProfile.objects.create(user=request.user,bio="",files="avater.png")
    context = {'profile':profile}
    if request.method=='POST':
        user_name= request.POST['username']
        photo = request.FILES['profile']
        bio = request.POST['bio']
        fname= request.POST['f_name']
        lname= request.POST['l_name']
        email= request.POST['email']
        pass1= request.POST['pass1']
        pass2= request.POST['pass2']
        if len(user_name) > 10 or len(user_name) < 5:
            messages.error(request,"Username must be under 5 to 10 characters!")
            return HttpResponseRedirect(reverse("myprofile", args=[request.user.username]))
        elif user_name.isalnum()==False:
            messages.error(request,"Username should only contain letters and numbers!")
            return HttpResponseRedirect(reverse("myprofile", args=[request.user.username]))
        elif pass1 != pass2:
            messages.error(request,"Passwords do not match!")
            return HttpResponseRedirect(reverse("myprofile", args=[request.user.username]))
        else:
            user = User.objects.get(username=username)
            user.username = user_name
            user.first_name = fname
            user.last_name = lname
            user.email = email
            user.set_password(str(pass1))
            login(request,user)
            user.save()
            fs = FileSystemStorage()
            fs.save(photo.name, photo)
            profile.files = photo.name
            profile.bio = bio
            profile.save()
            messages.error(request,"Profile successfully Updated!")
            try:
                return HttpResponseRedirect(reverse("myprofile", args=[request.user.username]))
            except:
                return redirect('myprofile', username=user_name)
    return render(request, 'myprofile.html',context)



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
    return render(request,'login.html')



def Logout(request):
    logout(request)
    messages.success(request,"Successfully logged out")
    return redirect("/")
    

def aboutus(request):

    return render(request, 'aboutus.html')
