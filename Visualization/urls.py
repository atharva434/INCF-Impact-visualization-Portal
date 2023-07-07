from django.contrib import admin
from django.urls import path,include
from Visualization import views
urlpatterns = [
    path("",views.home,name="home"),
    path("org",views.organization)
]