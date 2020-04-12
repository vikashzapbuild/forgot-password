from django.contrib import admin
from django.urls import path,include
 
from django.conf.urls import  url
from django.contrib.auth import views as auth_views
from .views import login_user
from django.contrib.auth import views as auth_views
from django.views.generic.base import TemplateView
urlpatterns=[
    #path('login/',login_user ),
    #path('accounts/login/',auth_views.LoginView.as_view(),name='login'),
    path('accounts/',include('django.contrib.auth.urls')),
    path('',TemplateView.as_view(template_name='home.html'),name='home')
]