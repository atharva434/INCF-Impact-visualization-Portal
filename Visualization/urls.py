from django.contrib import admin
from django.urls import path,include
from Visualization import views
urlpatterns = [
    path("adminpage",views.home,name="home"),
    path("",views.homepage),
    path("org",views.organization)
]