from . import views
from django.urls import path
from django.conf.urls import url
from django.views.generic.base import TemplateView

urlpatterns = [
    # ex: /polls/
    # path('', views.index, name='index'),
    # ex: /polls/5/
    # path('<int:question_id>/', views.detail, name='detail'),
    # ex: /polls/5/results/
    # path('<int:question_id>/results/', views.results, name='results'),
    
    url('total', views.cartpricecalculator,name='cartprice'),
    url('checkout',views.checkoutpage,name= "checkout"),
    url('updatePrefences',views.updatePref,name='pref update'),
    url('order',views.orderProcessing,name='orderprocessing'),
    url(r'^status/(?P<orderid>\d+)/$',views.orderStatus,name='orderstaus')
]