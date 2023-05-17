from django.shortcuts import render,HttpResponse,redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.decorators import login_required

# Create your views here.

def SignUp(request):
    if request.method=='POST':
        uname=request.POST['uname']
        email=request.POST['email']
        password=request.POST['pass']
        cpass=request.POST['cpass']


        if password!=cpass:
            return HttpResponse('Your password and confirm password doesnot match')
        
        else:
            myuser= User.objects.create_user(uname,email,password)
            myuser.save()
            return redirect('login')
    return render(request,'signup.html')

def LoginPage(request):
    if request.method=='POST':
        uname=request.POST['name']
        password=request.POST['pass']
        user=authenticate(request,username=uname,password=password)

        if user is not None:
            login(request,user)
            return redirect('Home')
        else:
            return HttpResponse("Username or Password is incorrect")
    return render(request,'login.html')

def LogoutPage(request):
    logout(request)
    return redirect('login')

@login_required(login_url='login')
def HomePage(request):
    return render(request,'home.html')

