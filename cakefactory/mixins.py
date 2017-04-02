from builtins import object
from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class PriceableMixin(object):

    def get_price(self):
        return self.price
