from django.urls import path
from django.conf.urls import url, include
from django.contrib.auth import views
from .views import *
from django.views.generic.base import TemplateView


urlpatterns = [
   
    path('', userView),
]
