from django.shortcuts import render, HttpResponse


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