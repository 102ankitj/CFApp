# Buisness-logic layer
# Provides connection between Data (Models) and UI(Templates)

# Importing Libraries
from builtins import super
from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.template import RequestContext
from django.contrib.auth.models import User
from django.views.generic import DetailView, ListView
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from django.contrib.auth import views as auth_views

from cakefactory.forms import RegistrationForm, AddCakeForm, BasketForm
from .models import Cake, Order, OrderItem

# Populates and processes data from the registration webpage
def registration_view(request):
    if request.method == "POST":
        form = RegistrationForm(request.POST)
        if form.is_valid():
            User.objects.create_user(
                username=form.cleaned_data.get('username'),
                password=form.cleaned_data.get('password'),
                email=form.cleaned_data.get('email'),
                first_name=form.cleaned_data.get('firstname'),
                last_name=form.cleaned_data.get('lastname'),
            )
            return render(request,
                          'registration/registration_completed.html')

    else:
        form = RegistrationForm()

    return render(request,
                  'registration/registration.html',
                  {'form': form},
                  RequestContext(request))

# Populates and processes data from the Cake List webpage
@method_decorator(login_required, name='dispatch')
class CakeListView(ListView):
    model = Cake
    template_name = "shop/CakeList.html"

# Populates and processes data from the selected cake deatils webpage
@method_decorator(login_required, name='dispatch')
class CakeDetailView(DetailView):
    model = Cake
    template_name = "shop/CakeDetail.html"
    form_class = AddCakeForm

    def get(self, request, **kwargs):
        form = self.form_class(initial={'cakeid': self.kwargs['pk']})
        cake = Cake.objects.get(id=self.kwargs['pk'])

        return render(request, self.template_name, {'form': form, 'cake': cake})

    def post(self, request, *args, **kwargs):
        form = self.form_class(request.POST)
        if form.is_valid():
            order, order_created = Order.objects.get_or_create(customer=request.user, current=True)

            oi, oi_created = OrderItem.objects.get_or_create(related_order=order,
                                                             product=Cake.objects.get(
                                                                 id=form.cleaned_data.get('cakeid')),
                                                             defaults={'quantity': form.cleaned_data.get('quantity')})
            if not oi_created:
                oi.quantity += form.cleaned_data.get('quantity')
                oi.save()

            order.items.add(oi)

            return HttpResponseRedirect('/basket/')

        return render(request, self.template_name, {'form': form})

    def get_context_data(self, **kwargs):
        context = super(CakeDetailView, self).get_context_data(**kwargs)
        return context

# Populates and processes data from the Basket webpage
@method_decorator(login_required, name='dispatch')
class OrderView(DetailView):
    model = Order
    template_name = "shop/OrderBasket.html"
    form_class = BasketForm

    def get(self, request, *args, **kwargs):
        form = self.form_class()
        order, created = Order.objects.get_or_create(customer=request.user, current=True)

        return render(request, self.template_name, {'form': form, 'order': order})


    def post(self, request, *args, **kwargs):
        form = self.form_class(request.POST)
        if form.is_valid():
            order = Order.objects.get(customer=request.user, current=True)
            order.address = form.cleaned_data.get('address')
            order.current = False
            order.save()

            return HttpResponseRedirect('/thx/')

        return render(request, self.template_name, {'form': form})

# Populates a webpage with Thank you message
def thx_view(request):
    return render(request, 'shop/thx.html')

# Populates a webpage with a welcome message
def homepage_view(request):
    return render(request, 'homepage.html')

def logout_view(request):
    return auth_views.logout(request, template_name='homepage.html')