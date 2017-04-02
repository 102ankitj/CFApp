# encoding: utf-8

from django.contrib.auth.models import User
from rest_framework import serializers, viewsets
from rest_framework.decorators import permission_classes
from rest_framework.permissions import IsAdminUser
from .models import Cake, Ingredient, Order, OrderItem

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
@permission_classes((IsAdminUser, ))
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
        fields = ('url', 'id', 'name', 'price')

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
        fields = ('url', 'id', 'name', 'price', 'weight', 'ingredients')

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
        fields = ('url', 'id', 'related_order', 'product', 'quantity')

# ViewSets define the view behavior.
@permission_classes((IsAdminUser, ))
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
        fields = ('url', 'id', 'address', 'customer', 'current', 'items')

# ViewSets define the view behavior.
@permission_classes((IsAdminUser, ))
class OrderViewSet(viewsets.ModelViewSet):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer

