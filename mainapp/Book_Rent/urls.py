from django.urls import path
from . import views

urlpatterns = [
    path('shop/', views.shopfun,name="shopurl"),
    path('sell/',views.sellfun,name="sellurl"),
    path('about/',views.aboutfun,name="abouturl"),
    path('contact/',views.contactfun,name="contacturl"),
    path('services/',views.servicesfun,name="servicesurl"),
    path('login/',views.loginfun,name="loginurl"),
    path('signup/',views.signupfun,name="signupurl"),
    path('logout/',views.logoutfun,name="logouturl"),
    path('booklist/',views.booklistfun,name="booklisturl"),
    path('product/',views.productfun,name="product.html"),
    path('book/<int:pk>/',views.bookfun,name='bookurl'),
    path('add/<int:sell_id>/', views.add_to_cart, name='add_to_cart'),
    path('remove/<int:item_id>/', views.remove_from_cart, name='remove_from_cart'),
    path('update/<int:item_id>/', views.update_cart, name='update_cart'),
    path('cart/', views.cart_detail, name='cart_detail'),

]