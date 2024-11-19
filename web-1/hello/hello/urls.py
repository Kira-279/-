"""
URL configuration for hello project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
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
from django.views.generic import TemplateView 
from django.contrib import admin 
from django.urls import path 
from django.urls import re_path 
from firstapp import views 

#urlpatterns = [ 
#    path('', views.index), 
#    re_path(r'^about', views.about), 
#    re_path(r'^contact', views.contact), 
#    path('products/<int:productid>/', views.products), 
#    path('users/', views.users), 
#] 

urlpatterns = [
    path('', views.index),
    re_path(r'^about', views.about),
    re_path(r'^contact', views.contact),
    path('products/', views.products), # маршрут по умолчанию
    path('products/<int:productid>/', views.products),
    path('users/', views.users), # маршрут по умолчанию
    path('users/<int:id>/<str:name>/', views.users),

#     path('products/<int:productid>/', views.products),
#     path('users/<int:id>/<name>/', views.users),
#    re_path(r'^products/(?P<productid>\d+)/', views.products),
#    re_path(r'^users/(?P<id>\d+)/(?P<name>\D+)/', views.users),
#    path('about/', TemplateView.as_view(template_name="firstapp/about.html")),
#    path('home/', TemplateView.as_view(template_name="firstapp/home.html")), 
#    path('contact/', TemplateView.as_view(template_name="firstapp/contact.html", extra_context={"work": "Разработка программных продуктов"})) 
]