#Contains URL Configuration and defines urlpatterns list which routes URLs to views

#Importing Libraries
from django.conf.urls import url, include
from django.contrib import admin
from django.contrib.auth import views as auth_views
from rest_framework import routers

from cakefactory.views import registration_view, CakeListView, CakeDetailView, OrderView, homepage_view, thx_view
from cakefactory.serializers import UserViewSet, CakeViewSet, IngredientViewSet, OrderItemViewSet, OrderViewSet


# Routers provide an easy way of automatically determining the URL conf.
router = routers.DefaultRouter()
router.register(r'users', UserViewSet)
router.register(r'cakes', CakeViewSet)
router.register(r'ingredients', IngredientViewSet)
router.register(r'orderitems', OrderItemViewSet)
router.register(r'orders', OrderViewSet)

urlpatterns = [
    url(r'^admin/', admin.site.urls),

    url(r'^accounts/login/$', auth_views.login, name='login'),
    url(r'^accounts/logout/$', auth_views.logout, name='logout'),
    url(r'^login/$', auth_views.login, name='login'),
    url(r'^logout/$', auth_views.logout, name='logout'),
    url(r'^signup/$', registration_view, name='registration'),

    url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    url(r'^api/', include(router.urls)),

    url(r'^home/$', homepage_view, name='homepage'),
    url(r'^accounts/profile/$', homepage_view, name='homepage'),

    url(r'^$', CakeListView.as_view(template_name="shop/CakeList.html"), name='root'),
    url(r'^cakes/$', CakeListView.as_view(template_name="shop/CakeList.html"), name='cakelist'),
    url(r'^cake/(?P<pk>\d+)$', CakeDetailView.as_view(template_name="shop/CakeDetail.html"), name='cake-details'),

    url(r'^basket/$', OrderView.as_view(template_name="shop/OrderBasket.html"), name='basket'),
    url(r'^thx/$', thx_view, name='thx'),
]
