from django.urls import path
from . import views 
from django.views.decorators.csrf import get_token


urlpatterns =  [
    path('restaurants/new/', views.create_a_new_restaurant, 
         name='create_a_new_restaurant'),

    path('restaurants/', views.get_all_restaurants, 
         name='get_all_restaurants'),

    path('restaurants/<int:restaurant_id>/', views.get_restaurant_by_id, 
         name='get_restaurant_by_id'),

    path('restaurants/patch/<int:restaurant_id>/', views.update_restaurant_by_id,
         name='update_restaurant_by_id'),
    
    path('restaurants/delete/<int:restaurant_id>/', views.delete_restaurant_by_id,
         name='delete_restaurant_by_id'),
     
    path('csrf-token/', get_token, name='api-csrf-token'),
]