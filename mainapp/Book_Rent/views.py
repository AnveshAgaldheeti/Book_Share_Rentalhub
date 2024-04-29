from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def shopfun(request):
    return render(request,'Base.html')

def sellfun(request):
    return HttpResponse('this is sell page')

def aboutfun(request):
    return HttpResponse('this is about page')

def servicesfun(request):
    return HttpResponse('this is services page')

def contactfun(request):
    return HttpResponse('this is contact page')
