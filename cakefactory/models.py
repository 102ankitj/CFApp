# Creating models for Cake, Orders, Basket and Ingredients a/c to the required attributes.

#Importing Libraries
from builtins import property  #Import built-in properties

from django.db import models  #Import pre-defined models in django framework
from django.contrib.auth.models import User  #Import User model from django models

from .mixins import PriceableMixin  #Import PriceableMixin from mixins.py


#Creating a model for cake with desired input fields
class Cake(models.Model, PriceableMixin):  #Creating a Model class object named Cake to contain specified attributes
    name = models.CharField(max_length=255)  #Enter the name of cake using a maximum of 255 characters only
    price = models.IntegerField()  #Set a price for the cake in whole numbers
    weight = models.IntegerField(blank=True,
                                 null=True)  #Set the weight of the cake in whole numbers. This field can be left empty
    ingredients = models.ManyToManyField(
        'Ingredient')  #Select the ingredients of the cake from Ingredients model. More than one ingredient can be chosen.

    #Funtion to set the return string from this model
    def __str__(self):
        return "{0}: {1}".format(self.name, self.price)  #Return the name and price of the cake when this model is used


#Creating a model for Basket
class OrderItem(models.Model):  #Creating a Model class object OrderItem
    related_order = models.ForeignKey(
        'Order')  #Set the order ID from Order model while the customer is shopping to store their selected cakes
    product = models.ForeignKey('Cake')  #Set the cake ID from Cake model to get its attributes like price
    quantity = models.IntegerField()  #Enter the quantity the customer wnats to purchase for the selected cake in whole numbers

    #Funtion to set the return string from this model
    def __str__(self):
        return "{0}: {1}".format(self.product,
                                 self.quantity)  #Return the ID for selected cake and desired quantity when this model is used

    #Function to get the price a/c to cake price and quantity
    @property
    def price(self):  #Function to calculate price
        return self.product.get_price() * self.quantity  #Return the price calculated by PriceMixin object in mixins.py


#Creating a model for Order
class Order(models.Model):  #Creating a Model class object named Order
    items = models.ManyToManyField('OrderItem')  #Set the items to be ordered from the basket model
    address = models.CharField(max_length=255,
                               null=True)  #Input the address of the customer using a maximum of 255 characters. The field is empty when the page is rendered
    customer = models.ForeignKey(User)  #Get the customer details from User model
    current = models.BooleanField(
        default=True)  #Check if the customer is still shopping. True if still shopping, False if customer is checking out

    #Function containing the algorithm to calculate the total price of all the items in the basket at checkout
    @property
    def price(self):
        sum = 0
        for oi in self.items.all():
            sum += oi.price

        return sum  #Return the calculated price


#Model to add new ingredients and set their prices. Cake prices are based on all the individual ingredient prices
class Ingredient(models.Model, PriceableMixin):  #Creating a Model class object called Ingredients
    name = models.CharField(max_length=255)  #Set the name of a new ingredient within 255 characters only
    price = models.IntegerField()  #Set the price of the new ingredient in whole numbers

    #Function to return the name and price of the ingredient when this model is used
    def __str__(self):
        return "{0}: {1}".format(self.name, self.price)


