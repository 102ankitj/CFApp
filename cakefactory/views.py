from builtins import super
from django.http import HttpResponseRedirect
from django.shortcuts import render, render_to_response
from django.template import RequestContext

from cakefactory.forms import RegistrationForm, AddCakeForm, BasketForm
from django.contrib.auth.models import User
from django.views.generic import TemplateView, DetailView, View
from django.views.generic import ListView
from django.core.exceptions import ObjectDoesNotExist
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator

from cakefactory.models import Cake, Order, OrderItem, Ingredient

def registration_view(request):

    if request.method=="POST":
        form = RegistrationForm(request.POST)
        if form.is_valid():
            User.objects.create_user(
                    username=request.POST['username'],
                    password=request.POST['password'],
                    email=request.POST['email'],
                    first_name=request.POST['firstname'],
                    last_name=request.POST['lastname'],
                    )
            return render(request,
                          'registration/registration_completed.html',)

    else:
        form = RegistrationForm()

    return render(request,
                  'registration/registration.html',
                  {'form':form},
                  RequestContext(request))


@method_decorator(login_required, name='dispatch')
class CakeListView(ListView):
    model = Cake
    template_name = "shop/CakeList.html"


@method_decorator(login_required, name='dispatch')
class CakeDetailView(DetailView):
    model = Cake
    template_name = "shop/CakeDetail.html"
    form_class = AddCakeForm

    def get(self, request, *args, **kwargs):
        form = self.form_class(initial={'cakeid': self.kwargs['pk']})
        cake = Cake.objects.get(id=self.kwargs['pk'])

        return render(request, self.template_name, {'form': form, 'cake': cake})

    def post(self, request, *args, **kwargs):
        form = self.form_class(request.POST)
        if form.is_valid():
            order, order_created = Order.objects.get_or_create(customer=request.user, current=True)

            oi, oi_created = OrderItem.objects.get_or_create(related_order=order,
                                                             product=Cake.objects.get(id=form.cleaned_data.get('cakeid')),
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
        print (request.POST)
        if form.is_valid():

            order = Order.objects.get(customer=request.user, current=True)
            order.address = form.cleaned_data.get('address')
            order.current = False
            order.save()

            return HttpResponseRedirect('/thx/')

        return render(request, self.template_name, {'form': form})


    def get_context_data(self, **kwargs):
        context = super(OrderView, self).get_context_data(**kwargs)
        return context

@method_decorator(login_required, name='dispatch')
class ThxView(DetailView):
    model = Order
    template_name = "shop/thx.html"


def homepage_view(request):
    return render(request, 'homepage.html')