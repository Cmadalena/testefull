"""lproject URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls')) createfuncionario
"""
from django.contrib import admin
from django.urls import path
from lapp.views import home, create, store, painel, dologin, dashboard, logouts, changePassword, flogin, createfuncionario, form

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', home, name='login'),
    path('create/', create, name='create'),
    path('store/', store, name='store'),
    path('painel/', painel, name='painel'),
    path('login/', flogin, name='flogin'),
    path('dologin/', dologin, name='dologin'),
    path('dashboard/', dashboard, name='dashboard'),
    path('logouts/', logouts, name='logouts'),
    path('password/', changePassword, name='password'),
    path('cadastrofuncionario/', form, name='cadastrofuncionario'),
    path('createfuncionario/', createfuncionario, name='createfuncionario'),
    #path('login/', home, name='home'),
]
