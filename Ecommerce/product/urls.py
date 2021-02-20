from django.urls import path
from .views import *

urlpatterns = [
    path('api/get_all_coffee_machines', get_all_coffee_machines, name='get_all_coffee_machines'),

    path('api/get_all_coffee_machines_by_type',
         get_all_coffee_machines_by_type, name='get_all_coffee_machines_by_type'),

    path('api/get_all_coffee_machines_by_water_line',
         get_all_coffee_machines_by_water_line, name='get_all_coffee_machines_by_water_line'),


    path('api/get_all_coffee_pods', get_all_coffee_pods, name='get_all_coffee_pods'),

    path('api/get_all_coffee_pods_by_type',
         get_all_coffee_pods_by_type, name='get_all_coffee_pods_by_type'),

    path('api/get_all_coffee_pods_by_flavor',
         get_all_coffee_pods_by_flavor, name='get_all_coffee_pods_by_flavor'),

    path('api/get_all_coffee_pods_by_pack_size',
         get_all_coffee_pods_by_pack_size, name='get_all_coffee_pods_by_pack_size'),
]
