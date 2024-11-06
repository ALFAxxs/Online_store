from django import forms
from .models import Item

class NewItemForm(forms.ModelForm):
    class Meta:
        model = Item
        fields = ('category', 'name', 'description', 'price', 'image',)

    category = forms.ChoiceField(widget=forms.Select(attrs={
        'class': 'w-full py-4 px-6 rounded-xl'
    }))

    name = forms.CharField(widget=forms.TextInput(attrs={
        'placeholder': 'name of product',
        'class': 'w-full py-4 px-6 rounded-xl'
    }))

    description = forms.CharField(widget=forms.Textarea(attrs={
        'placeholder': 'description of product',
        'class': 'w-full py-4 px-6 rounded-xl'
    }))

    price = forms.FloatField(widget=forms.NumberInput(attrs={
        'placeholder': 'price of item',
        'class': 'w-full py-4 px-6 rounded-xl'
    }))

    image = forms.ImageField(widget=forms.FileInput(attrs={
        'class': 'w-full py-4 px-6 rounded-xl'
    }))
