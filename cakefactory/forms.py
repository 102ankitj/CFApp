# encoding: utf-8

from django import forms
from django.forms.utils import ErrorList
from django.contrib.auth.models import User


# checks if username exists
# checks pass's are same
class RegistrationForm(forms.Form):
    username = forms.CharField()
    password = forms.CharField(widget=forms.PasswordInput)
    password2 = forms.CharField(widget=forms.PasswordInput)
    email = forms.EmailField()
    firstname = forms.CharField()
    lastname = forms.CharField()

    # Set CSS class for input fields
    username.widget.attrs.update({'class': 'form-control'})
    password.widget.attrs.update({'class': 'form-control'})
    password2.widget.attrs.update({'class': 'form-control'})
    email.widget.attrs.update({'class': 'form-control'})
    firstname.widget.attrs.update({'class': 'form-control'})
    lastname.widget.attrs.update({'class': 'form-control'})

    def clean(self):
        username = self.cleaned_data.get('username')
        password = self.cleaned_data.get('password')
        password2 = self.cleaned_data.get('password2')

        if not(password == password2):
            self.errors['password']=ErrorList([u"Passwords are not the same"])

        try:
            if not User.objects.get(username=username)==None:
                self.errors['username']=ErrorList([u"Too slow; This name already taken"])
        except:
            pass

        return self.cleaned_data


class SpecialCakeForm(forms.Form):
    # customer = forms.ModelChoiceField(User)
    ingredients = forms.MultipleChoiceField()
    description = forms.CharField()

    # customer.widget.attrs.update({'class': 'form-control'})
    ingredients.widget.attrs.update({'class': 'form-control'})


class AddCakeForm(forms.Form):
    cakeid = forms.IntegerField()
    quantity = forms.IntegerField(min_value=1)

    quantity.widget.attrs.update({'class': 'form-control'})


class BasketForm(forms.Form):
    # orderid = forms.IntegerField()
    address = forms.CharField()

    address.widget.attrs.update({'class': 'form-control'})