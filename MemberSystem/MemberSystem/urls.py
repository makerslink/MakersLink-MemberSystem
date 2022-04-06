"""MemberSystem URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from django.shortcuts import render
from django_registration.backends.activation.views import RegistrationView
from Members.forms import MemberRegistrationForm

def index(request):
    return render(request, 'base_menu.html')

def test(request):
    return render(request, 'base.html')

urlpatterns = [
    path('admin/', admin.site.urls),
    path('members/', include('Members.urls')),
    path('members/', include('Members.registration_urls')),
    #path('members/register/', RegistrationView.as_view(form_class=MemberRegistrationForm), name='django_registration_register'),
    #path('members/', include('django_registration.backends.activation.urls')),
    #path('accounts/', include('django_registration.backends.activation.urls')),
    #path('accounts/', include('django.contrib.auth.urls')),
    path('', index, name='index'),
    path('test', test, name='test'),
]