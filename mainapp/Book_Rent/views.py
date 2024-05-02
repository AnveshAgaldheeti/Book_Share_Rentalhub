from django.shortcuts import render,redirect
from django.http import HttpResponse
from .forms import Sell_form
from django.contrib import messages
from django.contrib.auth import authenticate,login,logout

def shopfun(request):
    return render(request,'Base.html')

def sellfun(request):
    form=Sell_form()
    if request.method=="POST":
        data=Sell_form(request.POST,request.FILES)
        if data.is_valid():
            data.save()
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
            return HttpResponse('logedin successfully')
        else:
            messages.error(request,'invalid credentials')
            redirect('loginurl')
    return render(request,'login.html')
