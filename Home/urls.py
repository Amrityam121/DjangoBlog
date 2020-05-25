from django.contrib import admin
from django.urls import path
from . import views
urlpatterns = [
    path('',views.Home,name="Home"),
    path('contacts',views.contacts,name="contacts"),
    path('about',views.about,name="about"),
    path('search',views.search,name="search"),
    path('Signup',views.Signup,name="Signup"),
    path('Login',views.handlelogin,name="Login"),
    path('Logout',views.handlelogout,name="Logout"),
]