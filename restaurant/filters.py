from .models import Cuisine, Restaurant
import django_filters

class CuisineFilter(django_filters.FilterSet):

    
    class Meta:
        model = Cuisine
        fields = ['Cuisine_parent']

# class AlphabeticalFilter(django_filters.FilterSet):
#     class Meta:
#         model = Restaurant