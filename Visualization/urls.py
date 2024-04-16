from django.contrib import admin
from django.urls import path,include
from Visualization import views
from django.contrib.auth.views import LogoutView
urlpatterns = [
    path("adminpage",views.home,name="home"),
    path("",views.homepage,name="homepage"),
    path("total",views.total_impact),
    path("org",views.organization),
    path("detail/<int:id>",views.detail),
    path("chatbot",views.chatbot, name="chatbot"),
    path('get_qa_model', views.get_qa_model, name='get_qa_model'),
    path("upload",views.upload),
    path("add/<int:id>",views.add),
    path("signup",views.signup,name="signup"),
    path("login",views.Login,name="login"),
    path("logout",LogoutView.as_view(next_page="login"),name="logout")
]