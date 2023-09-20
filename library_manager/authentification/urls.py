from django.urls import path
from . import views
from .forms import LoginFormm
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('login/',auth_views.LoginView.as_view(authentication_form = LoginFormm, template_name = 'authentification/login.html'), name = 'login' ),
    path('', views.signup, name='signup'),
    path('logout/', views.LogoutPage, name='logout'),
]
