from django.shortcuts import render,redirect,HttpResponse
from .models import *
from .forms import *
from django.contrib.auth import logout

# Create your views here.

def library(request):
    shelf=Book.objects.all()
    return render(request,'library.html',{'shelf':shelf})

def upload(request):
    upload=BookCreate()
    if request.method=='POST':
        upload = BookCreate(request.POST,request.FILES)
        if upload.is_valid():
            upload.save()
            return redirect('Home')
        else:
            return HttpResponse("""Something went wrong.Wait for a minute""")
    else:
        return render(request,'upload.html',{'upload_form':upload})
    

def update_book(request,book_id):
    book_id=int(book_id)
    try:
        book_shelf=Book.objects.get(id=book_id)
    except Book.DoesNotExist:
        return redirect('Home')
    book_form=BookCreate(request.POST or None, instance=book_shelf)
    if book_form.is_valid():
        book_form.save()
        return redirect('Home')
    return render(request,'upload.html',{'upload_form':book_form})

def delete_book(request,book_id):
    book_id=int(book_id)
    try:
        book_shelf=Book.objects.get(id=book_id)
    except Book.DoesNotExist:
        return redirect('Home')
    book_shelf.delete()
    return redirect('Home')

def LogoutPage(request):
    logout(request)
    return redirect('login')


