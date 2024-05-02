from django.shortcuts import render,redirect
from django.http import HttpResponse
from .forms import Sell_form,signupform
from django.contrib import messages
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.decorators import login_required

def shopfun(request):
    return render(request,'Base.html')

@login_required(login_url='loginurl')
def sellfun(request):
    form=Sell_form()
    if request.method=="POST":
        data=Sell_form(request.POST,request.FILES)
        if data.is_valid():
            new_book = data.save(commit=False)
            new_book.uploaded_by = request.user
            new_book.save()
            return HttpResponse("data inserted ")
        else:
            return HttpResponse("data not inserted")
    else:
        return render(request,'Sell.html',{"form":form})

def aboutfun(request):
    return HttpResponse('this is about page')

def servicesfun(request):
    return HttpResponse('this is services page')

def contactfun(request):
    return HttpResponse('this is contact page')

def loginfun(request):
    if request.method=='POST':
        uname=request.POST['username']
        pwd=request.POST['password']
        obj=authenticate(request,username=uname,password=pwd)
        if obj:
            login(request,obj)
            # return render(request,'formapp/displayimg.html',{'user':request.user})
            return redirect('shopurl')
        else:
            messages.error(request,'invalid credentials')
            redirect('loginurl')
    return render(request,'login.html')

def signupfun(request):
    empty=signupform()
    if request.method=='POST':
        obj=signupform(request.POST)
        if obj.is_valid()==True:
            user=obj.save()
            login(request,user)
            # messages.success(request,'loged in successfully')
            return redirect('loginurl')
        else:
            messages.error(request,' please enter valid details ')
            return render(request,'signup.html',{'form':obj})
    context={'form':empty}
    return render(request,'signup.html',context)

def logoutfun(request):
    logout(request)
    return redirect('loginurl')