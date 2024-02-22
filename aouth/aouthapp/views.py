from django.shortcuts import render,redirect
from .forms import *
from .models import *
from django.contrib.auth import logout

# Create your views here.


def index(request):
    if request.method=='POST':
        unm=request.POST['username']
        pas=request.POST['password']
        print(unm)
        print(pas)

        user=addsignup.objects.filter(username=unm,password=pas)                                                                                                                                                                                                
        if user: #TRUE
            print("Login Successfully!")
            request.session['user']=unm #create session
            return redirect('home')
        else:
            print("Error!Invalid username or password...")
    return render(request,'index.html')


def signup(request):
    if request.method=='POST':
        newuser=signupForm(request.POST)
        if newuser.is_valid():
            newuser.save()
            print("Signup Successfully!")
            return redirect('/')
        else:
            print(newuser.errors)
    return render(request,'signup.html')

def home(request):
    user=request.session.get('user')
    final = addsignup.objects.get(username=user)

    return render(request,'home.html',{'user':user,'final':final})


def userlogout(request):
    logout(request)
    return redirect('/')