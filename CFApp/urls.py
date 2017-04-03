#Contains URL Configuration and defines urlpatterns list which routes URLs to views

#Importing Libraries
from django.conf.urls import url, include			#Impoerting include and url classes for URL configuration
from django.contrib import admin					#Importing admin for the admin webpage
from django.contrib.auth import views as auth_views	#Importing auth-views to restrict access only to authorised users
from rest_framework import routers					#Routers provide an easy way of automatically determining the URL conf.

from cakefactory.views import registration_view, CakeListView, CakeDetailView, OrderView, homepage_view, thx_view, logout_view		#Importing views from views.py
from cakefactory.serializers import UserViewSet, CakeViewSet, IngredientViewSet, OrderItemViewSet, OrderViewSet			            #Importing ViewSets from serializers.py

#Registering all the viewsets on the router
router = routers.DefaultRouter()					#Creating a router class object named router
router.register(r'users', UserViewSet)				#Regular expression 'users' defines the routing of UserViewSet
router.register(r'cakes', CakeViewSet)				#Regular expression 'cakes' defines the routing of CakeViewSet
router.register(r'ingredients', IngredientViewSet)	#Regular expression 'ingredients' defines the routing of IngredientViewSet
router.register(r'orderitems', OrderItemViewSet)	#Regular expression 'orderitems' defines the routing of OrderItemViewSet
router.register(r'orders', OrderViewSet)			#Regular expression 'orders' defines the routing of OrderViewSet

#List containing all the URLs
urlpatterns = [
    url(r'^admin/', admin.site.urls),													#URL for admin webpage only accessible by administrator

    url(r'^accounts/login/$', auth_views.login, name='login'),							#URL for login webpage
    url(r'^accounts/logout/$', auth_views.logout, name='logout'),						#URL for logout webpage
    url(r'^login/$', auth_views.login, name='login'),									#Another URL for login webpage
    url(r'^logout/$', logout_view, name='logout'),								#Another URL for logout webpage
    url(r'^signup/$', registration_view, name='registration'),							#URL for registration webpage

    url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework')),		#URL for API webpage
    url(r'^api/', include(router.urls)),												#Include URLs from router in the API

    url(r'^home/$', homepage_view, name='homepage'),									#URL for home webpage
    url(r'^accounts/profile/$', homepage_view, name='homepage'),						#Another URL for home webpage

    url(r'^$', CakeListView.as_view(template_name="shop/CakeList.html"), name='root'),	#URL for Shop webpage showing the list of cakes which is also the root webpage
    url(r'^cakes/$', CakeListView.as_view(template_name="shop/CakeList.html"), name='cakelist'),	#Another URL for shop webpage
    url(r'^cake/(?P<pk>\d+)$', CakeDetailView.as_view(template_name="shop/CakeDetail.html"), name='cake-details'),	#URL for a webpage displaying the details of selected cake

    url(r'^basket/$', OrderView.as_view(template_name="shop/OrderBasket.html"), name='basket'),		#URL for basket webpage
    url(r'^thx/$', thx_view, name='thx'),												#URL for ThanksCheckout webpage
]
