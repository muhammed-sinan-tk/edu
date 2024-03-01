from django.contrib import admin
from django.urls import path,include
from . import views
app_name='web'
urlpatterns = [
    path("",views.index,name='index'),
    path("contact",views.contact,name='contact'),
    path("school",views.school,name='school'),
    path("about",views.about,name='about'),
    path("photo",views.photo,name='photo'),
    path("class",views.class1,name='class'),
]