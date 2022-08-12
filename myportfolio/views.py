from django.http import HttpResponse
from django.shortcuts import render
from django.core.mail import send_mail
from django.conf import settings

# Create your views here.

def index(request):
    title = 'manueljo home page'
    page = 'home'
    context = {'page':page, 'title':title}
    return render(request, 'index.html', context)

def about(request):
    title = 'manueljo about page'
    page = 'about'
    if request.method == 'POST':
        sender = request.POST['email']
        subject = request.POST['subject']
        message = request.POST['message']
        
        send_mail(
            subject,
            message,
            sender,
            ['dezin.mj@gmail.com']
        )
        
        
    context = {'page':page, 'title':title}
    return render(request, 'index.html', context)

def projects(request):
    title = 'manueljo projects and skills page'
    page = 'projects'
    context = {'page':page, 'title':title}
    return render(request, 'index.html', context)