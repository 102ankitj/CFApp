#Admin webpage which allows administrator to add/remove/edit users, cakes, ingredients, orders, user permissions and restrictions.

#Importing Libraries
from django.contrib import admin									#Import framework to automatically generate admin functions a/c to provided models
from cakefactory.models import Cake, Order, Ingredient, OrderItem	#Import models defined in models.py

#Registering models to be displayed and modified from the admin page of the website
admin.site.register(Cake)			#Register Cake model
admin.site.register(Order)			#Register Order model
admin.site.register(OrderItem)		#Register Order Item model
admin.site.register(Ingredient)		#Register Ingredient model