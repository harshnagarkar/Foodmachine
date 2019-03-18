from django.urls import path
from django.conf.urls import url, include
from django.contrib.auth import views
from authentication.views import makeUser, userView
from django.views.generic.base import TemplateView


urlpatterns = [
    path('', userView),
    # path('registration/', TemplateView.as_view(template_name = 'sgnup.html'))
    path('registration', makeUser)
]
