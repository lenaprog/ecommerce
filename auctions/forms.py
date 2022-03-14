from django import forms
from .models import Listing
from django.forms import TextInput, Textarea, URLInput, ChoiceField


class newListingForm(forms.ModelForm):
    class Meta:
        model = Listing
        fields = ["title", "description", "image", "starting_bid", "category", "date"]
        
        widgets = {
            "title" : TextInput(attrs={
                "class": "form-control;",
                "style": "max_width : 300px;",
                "placeholder": "title"
            }),

            "description": Textarea(attrs={
                "lablel": '',
                "class": "form-control;",
                "style": "max_width : 300px;",
                "placeholder": "describe your item"
            }),

            "image": URLInput(attrs={
                "class": "form-control;",
                "style": "max_width : 300px;",
                "placeholder": "upload image"
            }),

            
            "starting_bid": TextInput(attrs={
                "class": "form-control;",
                "style": "max_width : 300px;",
                "placeholder": "enter your starting bid"
            }),    

        }
