from django.urls import path
from . import views

urlpatterns = [
    path('home/', views.homefun,name="homeurl"),
    path('sell/',views.sellfun,name="sellurl"),
    path('about/',views.aboutfun,name="abouturl"),
    path('contact/',views.contactfun,name="contacturl"),
    path('services/',views.servicesfun,name="servicesurl"),

]