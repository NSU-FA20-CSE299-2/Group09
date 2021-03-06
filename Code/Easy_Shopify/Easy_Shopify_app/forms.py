from django import forms
from django.contrib.auth.models import User
from . import models

class CustomerUserForm(forms.ModelForm):
    class Meta:
        model=User
        fields=['first_name','last_name','username','password']
        widgets = {
        'password': forms.PasswordInput()
        }
        
class CustomerForm(forms.ModelForm):
    class Meta:
        model=models.Customer
        fields=['address','mobile']

class ProductForm(forms.ModelForm):
    class Meta:
        model=models.Product
        fields=['name','price','description','product_image']

class FeedbackForm(forms.ModelForm):
    class Meta:
        model=models.Feedback
        fields=['name','feedback']