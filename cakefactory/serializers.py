# encoding: utf-8

from django.contrib.auth.models import User
from rest_framework import routers, serializers, viewsets
from .models import Cake, Ingredient, Order, OrderItem
from rest_framework import permissions

##############################################################################

##     ##  ######  ######## ########
##     ## ##    ## ##       ##     ##
##     ## ##       ##       ##     ##
##     ##  ######  ######   ########
##     ##       ## ##       ##   ##
##     ## ##    ## ##       ##    ##
 #######   ######  ######## ##     ##

##############################################################################

class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ('url', 'username', 'email', 'is_staff')

# ViewSets define the view behavior.
class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer


##############################################################################

#### ##    ##  ######   ########  ######## ########  #### ######## ##    ## ########
 ##  ###   ## ##    ##  ##     ## ##       ##     ##  ##  ##       ###   ##    ##
 ##  ####  ## ##        ##     ## ##       ##     ##  ##  ##       ####  ##    ##
 ##  ## ## ## ##   #### ########  ######   ##     ##  ##  ######   ## ## ##    ##
 ##  ##  #### ##    ##  ##   ##   ##       ##     ##  ##  ##       ##  ####    ##
 ##  ##   ### ##    ##  ##    ##  ##       ##     ##  ##  ##       ##   ###    ##
#### ##    ##  ######   ##     ## ######## ########  #### ######## ##    ##    ##

##############################################################################

class IngredientSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Ingredient
        fields = ('name', 'price')

# ViewSets define the view behavior.
class IngredientViewSet(viewsets.ModelViewSet):
    queryset = Ingredient.objects.all()
    serializer_class = IngredientSerializer


##############################################################################

 ######     ###    ##    ## ########
##    ##   ## ##   ##   ##  ##
##        ##   ##  ##  ##   ##
##       ##     ## #####    ######
##       ######### ##  ##   ##
##    ## ##     ## ##   ##  ##
 ######  ##     ## ##    ## ########

##############################################################################

class CakeSerializer(serializers.HyperlinkedModelSerializer):
    ingredients = IngredientSerializer(read_only=True, many=True)

    class Meta:
        model = Cake
        fields = ('id', 'name', 'price', 'weight', 'ingredients')

# ViewSets define the view behavior.
class CakeViewSet(viewsets.ModelViewSet):
    queryset = Cake.objects.all()
    serializer_class = CakeSerializer



##############################################################################

 #######  ########  ########  ######## ########  #### ######## ######## ##     ##
##     ## ##     ## ##     ## ##       ##     ##  ##     ##    ##       ###   ###
##     ## ##     ## ##     ## ##       ##     ##  ##     ##    ##       #### ####
##     ## ########  ##     ## ######   ########   ##     ##    ######   ## ### ##
##     ## ##   ##   ##     ## ##       ##   ##    ##     ##    ##       ##     ##
##     ## ##    ##  ##     ## ##       ##    ##   ##     ##    ##       ##     ##
 #######  ##     ## ########  ######## ##     ## ####    ##    ######## ##     ##


##############################################################################

class OrderItemSerializer(serializers.HyperlinkedModelSerializer):

    class Meta:
        model = OrderItem
        fields = ('id', 'related_order', 'product', 'quantity')

# ViewSets define the view behavior.
class OrderItemViewSet(viewsets.ModelViewSet):
    queryset = OrderItem.objects.all()
    serializer_class = OrderItemSerializer




##############################################################################

 #######  ########  ########  ######## ########
##     ## ##     ## ##     ## ##       ##     ##
##     ## ##     ## ##     ## ##       ##     ##
##     ## ########  ##     ## ######   ########
##     ## ##   ##   ##     ## ##       ##   ##
##     ## ##    ##  ##     ## ##       ##    ##
 #######  ##     ## ########  ######## ##     ##

##############################################################################

class OrderSerializer(serializers.HyperlinkedModelSerializer):
    items = OrderItemSerializer(read_only=True, many=True)

    class Meta:
        model = Order
        fields = ('id', 'address', 'customer', 'current', 'items')

# ViewSets define the view behavior.
class OrderViewSet(viewsets.ModelViewSet):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer

