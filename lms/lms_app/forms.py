from django import forms
from .models import *

class CategoryForm(forms.ModelForm):
    class Meta:
        model = Category
        fields = ['name']
        widgets = {
            'name' : forms.TextInput(attrs={'class':'form-control'})
        }

class BookForm(forms.ModelForm):
    class Meta:
        model = Book
        fields = '__all__'
        widgets = {
            'rental_price_day' : forms.NumberInput(attrs={'id':'rentalprice'}),
            'rental_period' : forms.NumberInput(attrs={'id':'rentaldays'}),
            'total_rental' : forms.NumberInput(attrs={'id':'totalrental'})
        }


             