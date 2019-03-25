from django.urls import path
from django.conf.urls import url
from django.views.generic.base import TemplateView
from . import views

urlpatterns = [
    # ex: /polls/
    # path('', views.index, name='index'),
    # ex: /polls/5/
    # path('<int:question_id>/', views.detail, name='detail'),
    # ex: /polls/5/results/
    # path('<int:question_id>/results/', views.results, name='results'),
    # ex: /polls/5/vote/
    path('<slug:restaurantName>', views.restaurantPage),
    url('createmenu', TemplateView.as_view(template_name = 'create-menu.html'), name = 'menu create'),
    url('sucess.html',views.createMenuItems),
    url('create-restaurant.html', views.createRestaurant),
]
