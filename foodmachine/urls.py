"""foodmachine URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
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
from django.urls import path
from django.conf.urls import url, include
from django.contrib.auth import views
from .views import *

urlpatterns = [
    path('admin/', admin.site.urls),
	url(r'^login/$', views.LoginView.as_view(template_name='login/logn.html'), name='login'),
	#url(r'^login/$', views.login, name='login
	url(r'^logout/$', views.LogoutView.as_view(template_name='login/logn.html'), name='logout'),
    #url(r'^logout/$', views.logout, name='logout'),
    url(r'^auth/', include('social_django.urls', namespace='social')),  # <- Here
    url(r'^$',home , name='home'),
    # url(r'^ forgotpassword/$', .view.forgotpassword)

]
