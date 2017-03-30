from django.contrib import admin
from cakefactory.models import Cake, Order, Ingredient, OrderItem

# Register your models here.

admin.site.register(Cake)
admin.site.register(Order)
admin.site.register(OrderItem)
admin.site.register(Ingredient)