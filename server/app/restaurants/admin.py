from django.contrib import admin
from .models import Restaurant, Tag, Dish

class DishInLine(admin.TabularInline):
    model = Dish
    extra = 3

class RestaurantTagInLine(admin.TabularInline):
    model = Tag.restaurants.through
    extra = 3

class RestaurantAdmin(admin.ModelAdmin):
    fieldsets = [ 
        (None,              {'fields': ['name']}),
        (None,              {'fields': ['address']}),
        (None,              {'fields': ['latitude']}),
        (None,              {'fields': ['longitude']}),
    ]

    inlines = [DishInLine, RestaurantTagInLine]
    list_display = ('name', 'address', 'latitude', 'longitude')

class TagAdmin(admin.ModelAdmin):
    fieldSets = [
        (None, {'fields': ['name']}),
    ]

    inlines = [RestaurantTagInLine]
    
class DishAdmin(admin.ModelAdmin):
    fieldSets = [
        (None, {'fields': ['name']}),
        (None, {'fields': ['description']}),
        (None, {'fields': ['price']}),
        (None, {'fields': ['restaurant']}),
    ]

    list_display = ('name', 'description', 'price', 'restaurant')

admin.site.register(Restaurant, RestaurantAdmin)
admin.site.register(Tag, TagAdmin)
admin.site.register(Dish, DishAdmin)
# Register your models here.
