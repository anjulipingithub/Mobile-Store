from django import forms
from .models import *


class ProductForm(forms.Form):
    class Meta:
        model=Product
        fields='__all__'
        # exclude=["user"]
        # widgets={
        #     "title":forms.TextInput(label='product',widget=forms.TextInput(attrs={'class':'form-control'})),
        #     "price":forms.NumberInput(label='ammount',widget=forms.NumberInput(attrs={'class':'form-control'})),
        #     "discount_price":forms.NumberInput(label='discount_price',widget=forms.NumberInput(attrs={'class':'form-control'})),
        #     "description":forms.Textarea(label='description',widget=forms.Textarea(attrs={'class':'form-control'})),
        #     "category":forms.Textarea(label='description',widget=forms.Textarea(attrs={'class':'form-control'})),
            
        # }
    



class Quantity(forms.Form):
    quantity=forms.IntegerField()
    quantity=forms.IntegerField()



class PaymentForm(forms.Form):
    card_number = forms.CharField(label='Credit Card Number', max_length=16)
    expiration_date = forms.DateField(label='Expiration Date', widget=forms.DateInput(attrs={'type': 'date'}))
    security_code = forms.CharField(label='Security Code', max_length=3)

class OrderForm(forms.Form):
    class Meta:
        model = Buy
        fields = ['name', 'email', 'phone', 'address', 'product']