from django.db import models
from django.contrib.auth.models import User
from .mixins import PriceableMixin
# Create your models here.

class Cake(models.Model, PriceableMixin):
    name = models.CharField(max_length=255)
    price = models.IntegerField()
    weight = models.IntegerField(blank=True, null=True)
    ingredients = models.ManyToManyField('Ingredient')

    def __str__(self):
        return "{0}: {1}".format(self.name, self.price)


class OrderItem(models.Model):
    related_order = models.ForeignKey('Order')
    product = models.ForeignKey('Cake')
    quantity = models.IntegerField()

    def __str__(self):
        return "{0}: {1}".format(self.product, self.quantity)


class Order(models.Model):
    items = models.ManyToManyField('OrderItem')
    address = models.CharField(max_length=255, null=True)
    customer = models.ForeignKey(User)
    current = models.BooleanField(default=True)

    # class Meta:
    #     unique_together = ('customer', 'current',)


class Ingredient(models.Model, PriceableMixin):
    name = models.CharField(max_length=255)
    price = models.IntegerField()

    def __str__(self):
        return "{0}: {1}".format(self.name, self.price)


