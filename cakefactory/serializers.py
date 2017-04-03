#Serialize all the models into json for API

#Importing Libraries
from django.contrib.auth.models import User					#Import User model from django models
from rest_framework import serializers, viewsets			#Import serializer and viewsets for API and API user interface
from rest_framework.decorators import permission_classes	#Import permission class to allow or deny access to resources for different users
from rest_framework.permissions import IsAdminUser			#Import to identify and set permissions as True for admin users
from .models import Cake, Ingredient, Order, OrderItem		#Import models from models.py

#Creating serializer and viewset for User model
class UserSerializer(serializers.HyperlinkedModelSerializer):	#Creating a serializer class object named UserSerializer
    class Meta:													#Service class
        model = User											#Set model as User model
        fields = ('url', 'username', 'email', 'is_staff')		#Specify the fields to be viewed in User API

# ViewSets define the view behavior.
@permission_classes((IsAdminUser, ))						#Only accessible by admin users
class UserViewSet(viewsets.ModelViewSet):					#Creating a viewset class object called UserViewSet
    queryset = User.objects.all()							#Load all the objects from User model into queryset
    serializer_class = UserSerializer						##Use UserSerializer to represent this ViewSet

#Creating serializer and viewset for Ingredients model
class IngredientSerializer(serializers.HyperlinkedModelSerializer):		#Creating a serializer class object named IngredientSerializer
    class Meta:															#Service class
        model = Ingredient												#Set model as Ingredients model
        fields = ('url', 'id', 'name', 'price')							#Specify the fields to be viewed in Ingredients API

#ViewSets define the view behavior.
class IngredientViewSet(viewsets.ModelViewSet):							#Creating a viewset class object called IngredientsViewSet
    queryset = Ingredient.objects.all()									#Load all the objects from Ingredients model into queryset
    serializer_class = IngredientSerializer								#Use IngredientSerializer to represent this ViewSet

#Creating serializer and viewset for Cake model
class CakeSerializer(serializers.HyperlinkedModelSerializer):				#Creating a serializer class object named CakeSerializer
    ingredients = IngredientSerializer(read_only=True, many=True)			#Initializing Ingredients as it's many to many field object;
																			#set as read only and allows many to many relations 
    class Meta:																#Service class
        model = Cake														#Set model as Cake model
        fields = ('url', 'id', 'name', 'price', 'weight', 'ingredients')	#Specify the fields to be viewed in Cake API

# ViewSets define the view behavior.
class CakeViewSet(viewsets.ModelViewSet):					#Creating a viewset class object called CakeViewSet
    queryset = Cake.objects.all()							#Load all the objects from Cake model into queryset
    serializer_class = CakeSerializer						#Use CakeSerializer to represent this ViewSet

#Creating serializer and viewset for OrderItem model
class OrderItemSerializer(serializers.HyperlinkedModelSerializer):		#Creating a serializer class object named OrderItemSerializer
    class Meta:															#Service class
        model = OrderItem												#Set model as OrderItem model
        fields = ('url', 'id', 'related_order', 'product', 'quantity')	#Specify the fields to be viewed in OrderItem API

# ViewSets define the view behavior.
@permission_classes((IsAdminUser, ))				#Only accessible by admin users
class OrderItemViewSet(viewsets.ModelViewSet):		#Creating a viewset class object called OrderItemViewSet
    queryset = OrderItem.objects.all()				#Load all the objects from OrderItem model into queryset
    serializer_class = OrderItemSerializer			#Use OrderItemSerializer to represent this ViewSet

#Creating serializer and viewset for Order model
class OrderSerializer(serializers.HyperlinkedModelSerializer):				#Creating a serializer class object named OrderSerializer
    items = OrderItemSerializer(read_only=True, many=True)					#Initializing OrderItems as it's many to many field object;
																			#set as read only and allows many to many relations
    class Meta:																#Service class
        model = Order														#Set model as Order model
        fields = ('url', 'id', 'address', 'customer', 'current', 'items')	#Specify the fields to be viewed in Order API

# ViewSets define the view behavior.
@permission_classes((IsAdminUser, ))			#Only accessible by admin users
class OrderViewSet(viewsets.ModelViewSet):		#Creating a viewset class object called OrderViewSet
    queryset = Order.objects.all()				#Load all the objects from Order model into queryset
    serializer_class = OrderSerializer			#Use OrderSerializer to represent this ViewSet

