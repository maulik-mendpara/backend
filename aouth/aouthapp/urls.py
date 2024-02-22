from django.contrib import admin
from django.urls import path,include
from aouthapp import views

urlpatterns = [
   path('',views.index),
   path('signup/',views.signup),
   path('home/',views.home,name='home'),
   path('userlogout/',views.userlogout),
]