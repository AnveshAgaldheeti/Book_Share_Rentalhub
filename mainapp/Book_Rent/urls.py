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
]