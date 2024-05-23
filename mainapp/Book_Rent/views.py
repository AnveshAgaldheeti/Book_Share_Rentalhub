from django.shortcuts import render,redirect,get_object_or_404
from django.http import HttpResponse
from .forms import Sell_form,signupform
from django.contrib import messages
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.decorators import login_required
from .models import Sell_model,Category,Cart,CartItem

def shopfun(request):
    new_arrival=Sell_model.objects.order_by("-date")[:3]
    return render(request,'Base.html',{"new_arrival":new_arrival})

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
            return render(request,'sell.html',{"form":data})
    else:
        return render(request,'Sell.html',{"form":form})

def aboutfun(request):
    return HttpResponse('this is about page')

def servicesfun(request):
    return render(request,'services.html')

def contactfun(request):
    return render(request,'contact.html')

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

def booklistfun(request):
    books=Sell_model.objects.all()
    categories=Category.objects.all()
    return render(request,'booklist.html',{'books':books,"categories":categories})


def productfun(request):
    return render(request,'product.html')

def bookfun(request,pk):
    b=Sell_model.objects.get(id=pk)
    return render(request,'book.html',{'book':b})

@login_required
def add_to_cart(request, sell_id):
    sell = get_object_or_404(Sell_model, id=sell_id)
    cart, created = Cart.objects.get_or_create(user=request.user)
    cart_item, created = CartItem.objects.get_or_create(cart=cart, sell=sell)

    if not created:
        cart_item.quantity += 1
    cart_item.save()
    return redirect('carturl')

@login_required
def remove_from_cart(request, item_id):
    cart_item = get_object_or_404(CartItem, id=item_id)
    cart_item.delete()
    return redirect('cart_detail')

@login_required
def update_cart(request, item_id):
    cart_item = get_object_or_404(CartItem, id=item_id)
    quantity = request.POST.get('quantity')
    if quantity and int(quantity) > 0:
        cart_item.quantity = int(quantity)
        cart_item.save()
    else:
        cart_item.delete()
    return redirect('cart_detail')

@login_required
def cart_detail(request):
    cart, created = Cart.objects.get_or_create(user=request.user)
    return render(request, 'cart/cart_detail.html', {'cart': cart})