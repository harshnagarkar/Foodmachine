from django.shortcuts import render
from .models import Restaurant, Menu
# Create your views here.
def Menu(request):
    return render(request, 'retaurant-menu')