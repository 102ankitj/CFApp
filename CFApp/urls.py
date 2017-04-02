"""CFApp URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.10/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url, include
from django.contrib import admin
from django.contrib.auth import views as auth_views
from rest_framework import routers

from cakefactory.views import registration_view, CakeListView, CakeDetailView, OrderView, homepage_view
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

    # url(r'^addcake/(?P<pk>\d+)$', CakeDetailView.as_view(template_name="shop/CakeDetail.html"), name='add-to-cart'),

    url(r'^basket/$', OrderView.as_view(template_name="shop/OrderBasket.html"), name='basket'),
    url(r'^thx/$', CakeListView.as_view(template_name="shop/thx.html"), name='thx'),
]
