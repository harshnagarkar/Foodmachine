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
from django.urls import path, include
from django.conf.urls import url, include
# from django.contrib.auth import views
from .views import home #test
from django.views.generic.base import TemplateView
from restaurant.views import Menu
from django.contrib.auth import views as auth_views
from django.conf import settings
from django.conf.urls import url, include
from django.conf.urls.static import static
# from django.contrib.auth.views import password_reset, password_reset_done
# from . import views

urlpatterns = [
    path('admin/', admin.site.urls),

    
    url(r'^login/$', auth_views.LoginView.as_view(template_name='login.html'),name='login'),
	# url(r'^login/$', views.LoginView.as_view(template_name = 'logn.html'), name = 'login'),
    url('restaurant/', include('restaurant.urls')),
    url('dashboard', include('authentication.urls')),
    url(r'^logout/$', auth_views.LogoutView.as_view(template_name='login.html'), name='logout'),
    #url(r'^logout/$', views.logout, name='logout'),
    url(r'^auth/', include('social_django.urls', namespace='social')),  # <- Here

    url(r'^$', home, name='home'),
    path('accounts/', include('django.contrib.auth.urls')),
	url('^', include('django.contrib.auth.urls'))

    #url(r'^change-password/$', views.change_password, name = 'change_password')) 
   
    #  (r'^media/(?P<path>.*)$', 'django.views.static.serve',
    #   {'document_root': settings.MEDIA_ROOT}),
    #  )
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

# if settings.DEBUG:
    # urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
