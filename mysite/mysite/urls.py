"""mysite URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
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
#urls.py
from django.contrib import admin  
from django.urls import path  
from myapp import views  
from django.conf.urls import url
 
urlpatterns = [  
    path('admin/', admin.site.urls),  
    path('',views.index),
    path('orders',views.orders, name='orders'),
    path('contact',views.contact, name='contact'),
    path('views',views.views, name='views'),
    path('changeorder',views.changeorder, name='changeorder'),
    path('cancelorder',views.cancelorder, name='cancelorder'),
    url(r'^create$', views.create, name='create'),
    url(r'^edit/(?P<id>\d+)$', views.edit, name='edit'),
    url(r'^edit/update/(?P<id>\d+)$', views.update, name='update'),
    url(r'^delete/(?P<id>\d+)$', views.delete, name='delete'),
] 

