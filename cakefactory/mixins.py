#Function to calculate the total price of all the items in customers basket

#Importing Librarries
from builtins import object						#Import built-in objects
from django.db import models					#Import pre-defined models in django framework
from django.contrib.auth.models import User		#Import User model from django models

#Creating a class to contain the price calculation function 
class PriceableMixin(object):

    def get_price(self):						#Defining price calculation function
        return self.price						#Return the calculated price whenever function is called
