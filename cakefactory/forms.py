#Creating webforms for user registration, shopping for cakes and a basket to hold items until customer checkout.

#Importing Libraries:
from django import forms						#Import Forms from django framework
from django.forms.utils import ErrorList		#Import ErrorList to generate errors in CSS
from django.contrib.auth.models import User		#Import User class from pre-defined models in django framework

#Creating a User Registration Form:
class RegistrationForm(forms.Form):								#Creating an object named RegistrationForm from imported forms to contain specified attributes
    username = forms.CharField()								#Creates a character field and stores the input in username
    password = forms.CharField(widget=forms.PasswordInput)		#Creates a Password field as a widget to contain pre-defined syntax validated values
    password2 = forms.CharField(widget=forms.PasswordInput)		#Adding another field of password using same specifications for password confirmation
    email = forms.EmailField()									#Creating a field for customer e-mail addresses with pre-defined e-mail syntax validation 
    firstname = forms.CharField()								#Creates a character field and stores the input as firstname of the user
    lastname = forms.CharField()								#Creates a character field and stores the input as lastname of the user

	#Add all the created fields to the webform using widgets & set CSS class for input fields
    username.widget.attrs.update({'class': 'form-control'})
    password.widget.attrs.update({'class': 'form-control'})
    password2.widget.attrs.update({'class': 'form-control'})
    email.widget.attrs.update({'class': 'form-control'})
    firstname.widget.attrs.update({'class': 'form-control'})
    lastname.widget.attrs.update({'class': 'form-control'})

	#Clean the data to remove any fonts and convert it to plain text
    def clean(self):											#Defining a function to clean the current class
        username = self.cleaned_data.get('username')			#Clean the input value in username field and store it in username
        password = self.cleaned_data.get('password')			#Clean the input value in password field and store it in password
        password2 = self.cleaned_data.get('password2')			#Clean the input value in password2 field and store it in password2

        if not(password == password2):														#If values in password and password2 are not similar, do:
            self.errors['password']=ErrorList([u"Passwords are not the same"])				#Generate an error in unicode using ErrorList to alert the user

        try:																				
            if not User.objects.get(username=username)==None:								#If the value in username is already present in previous User object usernames, do:
                self.errors['username']=ErrorList([u"Too slow; This name already taken"])	#Generate an error in unicode using ErrorList to alert the user
        except:
            pass																			#If both the above conditions are satisfied, then proceed.

        return self.cleaned_data								#Return the cleaned data with the form when it is submitted

#Creating a Form to store selected cake and quantity when shopping:		
class AddCakeForm(forms.Form):									#Creating an object named AddCakeForm from imported forms to contain specified fields
    cakeid = forms.IntegerField()								#Creating an integer field to store the unique ID of the selected cake
    quantity = forms.IntegerField(min_value=1)					#Creating an integer field to specify the required quantity of the selected cake and setting the minimum quantity to 1

    quantity.widget.attrs.update({'class': 'form-control'})		#Creating a widget to input the quantity field on the webform

#Creating a form to obtain the delivery address of customer before checkout
class BasketForm(forms.Form):									#Creating an object named BasketForm from imported forms to contain specified attributes
    address = forms.CharField()									#Creating a character field to store the delivery address of the customer

    address.widget.attrs.update({'class': 'form-control'})		#Creating a widget to input the delivery address on the rendered webform