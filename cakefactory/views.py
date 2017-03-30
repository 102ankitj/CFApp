from builtins import super
from django.http import HttpResponseRedirect
from django.shortcuts import render, render_to_response
from django.template import RequestContext

from cakefactory.forms import RegistrationForm, AddCakeForm
from django.contrib.auth.models import User
from django.views.generic import TemplateView, DetailView, View
from django.views.generic import ListView

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



class CakeListView(ListView):
    model = Cake
    template_name = "shop/CakeList.html"



class CakeDetailView(DetailView):
    model = Cake
    template_name = "shop/CakeDetail.html"
    form_class = AddCakeForm

    def get(self, request, *args, **kwargs):
        form = self.form_class(initial={'cakeid': self.kwargs['pk']})
        # print (Cake.objects.get(kwargs['pk']).ingredients.all())
        cake = Cake.objects.get(id=self.kwargs['pk'])

        return render(request, self.template_name, {'form': form, 'cake': cake})

    def post(self, request, *args, **kwargs):
        form = self.form_class(request.POST)
        # print(form.cakeid)
        # print(form.quantity)
        print (request.POST)
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
        # # context.update({
        # #     'form': self.form
        # # })
        # context['form'] = self.form
        return context



class OrderView(DetailView):
    model = Order
    template_name = "shop/OrderBasket.html"

    def get(self, request, *args, **kwargs):

        order = Order.objects.get(customer=request.user, current=True)

        return render(request, self.template_name, {'order': order})

    def get_context_data(self, **kwargs):
        context = super(OrderView, self).get_context_data(**kwargs)
        return context




class OrderDetailView(DetailView):
    pass

# class CakeAddView(DetailView):
#     model = Cake
#     template_name = "shop/CakeDetail.html"
#
#     def get_context_data(self, **kwargs):
#         context = super(CakeDetailView, self).get_context_data(**kwargs)
#         return context

#
# class CakeAddView(View):
#     form_class = AddCakeForm
#     # initial = {'key': 'value'}
#     # template_name = 'form_template.html'
#
#     # def get(self, request, *args, **kwargs):
#     #     form = self.form_class(initial=self.initial)
#     #     return render(request, self.template_name, {'form': form})
#
#     def post(self, request, *args, **kwargs):
#         form = self.form_class(request.POST)
#         if form.is_valid():
#             return HttpResponseRedirect('/success/')
#
#         return render(request, self.template_name, {'form': form})