from django.shortcuts import render
from django.http import HttpResponse
from django.core import serializers
from django.http import Http404, HttpResponseNotAllowed
from .models import Restaurant, Dish, Tag
import json

def create_a_new_restaurant(request):
    if request.method == 'POST':
        body = json.loads(request.body.decode('utf-8'))
        new_name = body.get("name")
        new_address = body.get("address")
        new_latitude = body.get("latitude")
        new_longitude = body.get("longitude")
        try:
            tag = Tag.objects.get(pk=body.get("tag_id"))
        except Tag.DoesNotExist:
            raise Http404("Tag does not exist")
        new_restaurant = Restaurant(name=new_name, address=new_address, latitude=new_latitude, longitude=new_longitude)
        new_restaurant.save()
        tag.restaurants.add(new_restaurant)
        tag.save()
        return HttpResponse(status=200)
    else:
        raise HttpResponseNotAllowed("Method is not supported")

def get_all_restaurants(request):
    query_set = Restaurant.objects.all()
    data = serializers.serialize('json', query_set)
    return HttpResponse(data)

def get_restaurant_by_id(request, restaurant_id):
    try:
        query_set = Restaurant.objects.filter(pk=restaurant_id)
    except Restaurant.DoesNotExist:
        raise Http404("Restaurant does not exist")
        data = serializers.serialize("json", query_set)
    return HttpResponse(data)

def update_restaurant_by_id(request, restaurant_id):
    if request.method == 'PUT':
        body = json.loads(request.body.decode('utf-8'))
        new_name = body.get("name")
        new_address = body.get("address")
        new_latitude = body.get("latitude")
        new_longitude = body.get("longitude")

        try:
            tag = Tab.objects.get(pk=body.get("tag_id"))
        except:
            raise Http404("Tag does not exist")
        
        restaurant.name = new_name
        restaurant.address = new_address
        restaurant.latitude = new_latitude
        restaurant.longitude = new_longitude
        restaurant.save()

        tag.restaurants.add(restaurant)
        tag.save()

        return HttpResponse(status=200)

    else:
        raise HttpResponseNotAllowed("Method is not supported")        

def delete_restaurant_by_id(request, restaurant_id):
    if request.method == 'DELETE':
        try:
            restaurant = Restaurant.objects.get(pk=restaurant_id)
        except Restaurant.DoesNotExist:
            raise Http404("Restaurant does not exist")

        message = {
            "message": "Deleted Restaurant"}

        # resp = message.json()
        # data = serializers.serialize("json", message)
        restaurant.delete()
        return HttpResponse(message)
    else:
        raise HttpResponseNotAllowed("Method is not supported")





# Create your views here.
