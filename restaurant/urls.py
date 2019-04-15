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

    path('<slug:restaurantName>', views.restaurantPage),
    url('createmenu/', TemplateView.as_view(template_name = 'create-menu.html'), name = 'menu_create'),
    url('createRestaurant',TemplateView.as_view(template_name='restaurant/createRestaurant.html'), name = "create_Restaurant"),
    url('sucessRestaurant', views.createRestaurant),
    url('createmenu', TemplateView.as_view(template_name="create-menu.html"),name='createformmenu'),
    url('createdmenu', views.createMenuItems, name='createdmenu'),
    url('delete_menu/', views.menuDelete, name = "menuDeleted")
]