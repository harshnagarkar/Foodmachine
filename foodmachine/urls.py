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
# from django.contrib.auth import views
from .views import home #test
from django.views.generic.base import TemplateView
from restaurant.views import Menu
from django.contrib.auth import views as auth_views
 
urlpatterns = [
    path('admin/', admin.site.urls),

    # path('registration/', register, name = 're'),
    # path('reset-password/', reset, name = 'reset'),
    # path('forgot-password/', forgot, name = 'forgot'),
    #path('', TemplateView.as_view(template_name='home.html'), name='home'),
    #url(r'^signup/$', views.SignUp.as_view(), name = 'signup'),
	#url(r'^login/$', views.LoginView.as_view(template_name='registration/login.html'), name='login'),
    # url(r'^login/$', auth_views.login),
    # url(r'^login/$', auth_views.login, {'template_name': 'logn.html'}),
    # path('Menus/', Menu, name = 'menu'),
    #url('test', test,name='test'),
    url(r'^login/$', auth_views.LoginView.as_view(template_name='logn.html'),name='login'),
	# url(r'^login/$', views.LoginView.as_view(template_name = 'logn.html'), name = 'login'),
    url('restaurant/', include('restaurant.urls')),
    url('dashboard', include('authentication.urls')),
  	# url(r'^login/$', views.LoginView.as_view(template_name='login.html'), name='login'),
	#url(r'^loginPageIndex/$', views.LoginView.as_view(template_name = 'loginPageIndex.html'), name = 'log'),
	#url(r'^login/$', views.login, name='login
	url(r'^logout/$', auth_views.LogoutView.as_view(template_name='login.html'), name='logout'),
    #url(r'^logout/$', views.logout, name='logout'),
    url(r'^auth/', include('social_django.urls', namespace='social')),  # <- Here

    url(r'^$', home, name='home'),
	#url(r'^$', TemplateView.as_view(template_name = 'loginPageIndex.html'), name = 'login'), #<-- Set Root Page to Login; must change later to dashboard
	#url(r'^S', views.LoginView.as_view(template_name = 'LoginPageIndex.html'), name = 'login'),
	
	#url(r'^password_reset/$', password_reset, name = 'password_reset'),  #Working on password reset here
	
]
	
