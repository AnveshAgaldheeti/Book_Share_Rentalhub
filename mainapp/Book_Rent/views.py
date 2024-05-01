from django.shortcuts import render
from django.http import HttpResponse
from .forms import Sell_form
from django.contrib import messages

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
