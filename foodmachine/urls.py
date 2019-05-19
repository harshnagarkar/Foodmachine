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

from .views import home
from django.views.generic.base import TemplateView
from restaurant.views import Menu
from django.contrib.auth import views as auth_views
from django.conf import settings
from django.conf.urls import url, include
from django.conf.urls.static import static
from django.views.generic import RedirectView


urlpatterns = [
    url('admin/', admin.site.urls),
    url(r'^accounts/profile/$', RedirectView.as_view(url='/')),
    url(r'^login/$', auth_views.LoginView.as_view(template_name='registration/lognn.html'), name='login'),
    url('restaurant/', include('restaurant.urls')),
    url('dashboard', include('authentication.urls')),
    url('cart/', include('orders.urls')),
    url(r'^logout/$', auth_views.LogoutView.as_view(
        template_name='registration/lognn.html'), name='logout'),
    url(r'^auth/', include('social_django.urls', namespace='social')),
    url('404', TemplateView.as_view(template_name='404.html'), name='404'),
    url(r'^$', home, name='home'),
    url('^', include('django.contrib.auth.urls')),
    url(r'password_change/$', auth_views.PasswordChangeView.as_view(
        template_name='registration/password_reset_form.html', success_url='/password_change_done')),
    url(r'password_change_done/', auth_views.PasswordChangeDoneView.as_view(
        template_name='registration/password_reset_done.html')),
    url(r'password_reset/$', auth_views.PasswordResetView.as_view(template_name='password_reset.html', email_template_name='registration/password_reset_email.html',
                                                                  subject_template_name='registration/password_reset_email.html', success_url='/password_reset_done/', from_email='admin@foodmachine.ml')),
    url(r'password_reset_done/', auth_views.PasswordResetDoneView.as_view(
        template_name='registration/password_reset_done.html')),
    url(r'password_reset_confirm/(?P<uidb64>[0-9A-Za-z_\-]+)/(?P<token>[0-9A-Za-z]{1,13}-[0-9A-Za-z]{1,20})/$', auth_views.PasswordResetConfirmView.as_view(
        template_name='registration/password_reset_confirm.html', success_url='registration/password_reset_complete.html')),

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
