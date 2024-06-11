from django.test import TestCase, client
from .models import Restaurant, Dish, Tag
import json

# Create your tests here.

class RestaurantModelTests(TestCase):
    def setUp(self):
        Restaurant.objects.create(name='test', address='test', latitude=0, longitude=0)

    def test_string_representation(self):
        restaurant = Restaurant.objects.get(id=1)
        self.assertEqual(str(restaurant), 'test')

class DishModelTests(TestCase):
    def setUp(self):
        Restaurant.objects.create(name='test', address='test', latitude=0, longitude=0)
        Dish.objects.create(name='test', description='test', price=0, restaurant=Restaurant.objects.get(id=1))

    def test_string_representation(self):
        dish = Dish.objects.get(id=1)
        self.assertEqual(str(dish), 'test')

    def test_price(self):
        dish = Dish.objects.get(id=1)
        self.assertEqual(dish.price, 0)
# Create your tests here.

class TagModelTests(TestCase):
    def setUp(self):
        Tag.objects.create(name='test')

    def test_string_representation(self):
        tag = Tag.objects.get(id=1)
        self.assertEqual(str(tag), 'test')


class ApiTests(TestCase):

    def setUp(self):
        self.client = client.Client()
        Restaurant.objects.create(name='test', address='test', latitude=0, longitude=0)

    def test_create_a_new_restaurant(self):
        # restaurant  = Restaurant.objects.get(id=1)
        restaurant = {
            'name': 'Test Restaurant',
            'address': 'Test Address',
            'latitude': 0,
            'longitude': 0
        }
        payload = json.dumps(restaurant)
        resp = self.client.post('/api/restaurants/new/', payload, content_type='application/json')
        self.assertEqual(resp.status_code, 200)

    def test_get_all_restaurants(self):
        resp = self.client.get('/api/restaurants/')
        self.assertEqual(resp.status_code, 200)

    def test_get_restaurant_by_id(self):
        pass
    def test_update_restaurant_by_id(self):
        pass
    def test_delete_restaurant_by_id(self):
        pass

