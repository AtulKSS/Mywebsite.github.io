from django import forms
from django.contrib import messages
from django.http.response import HttpResponse
from django.shortcuts import redirect, render, HttpResponse
from home.models import Contact
from django.contrib import messages
from django.contrib.auth import authenticate , login
from django.contrib.auth.models import User
from django.contrib.auth import logout
def index(request):
    if request.user.is_anonymous:
        return redirect("/login")
    return render(request,'index.html') 
def contact(request):
    if request.method == "POST":
        name = request.POST.get('name')
        email = request.POST.get('email')
        phone = request.POST.get('phone')
        desc = request.POST.get('desc')
        if len(name)<2 or len(email)<3 or len(phone)<10 or len(desc)<5:
            messages.error(request,"Please fill form correctly")
        else:
            contact = Contact(name=name , email=email, phone=phone, desc=desc) 
            contact.save()
            messages.info(request, 'Your request has been sent')
    return render(request ,'contact.html')
    # return HttpResponse("this is contact")

def about(request):
    return render(request,'about.html' )

def link(request):
    return render(request,'link.html')
    
def loginuser(request):
    if request.method=="POST":
        username=request.POST.get('naam')
        password=request.POST.get('passs')

        user = authenticate(username=username, password=password)
        if user is not None:
            login(request , user)
            return redirect("/loggedinn")
        else:
            messages.info(request, 'Wrong username or password or sign up')
     
        
    return render(request,'login.html')

def logoutuser(request):
    logout(request)
    return redirect("/")

def signup(request):
    if request.method=="POST":
        names=request.POST.get("nave")
        emails=request.POST.get('eeemail')
        passwor=request.POST.get('passwor')

        if User.objects.filter(username = names).first():
            messages.error(request, "This username is already taken") 
        elif len(names)<2 or len(emails)<3 or len(passwor)<50:
            messages.info(request, "Enter the details")  
        else:

            user = User.objects.create_user(names ,emails ,passwor)
            messages.info(request, "Account Created Sucessfully")

        print(names,emails,passwor)  
    return render(request, 'signup.html')

def logged(request):
    return render(request,'loggedinn.html')  