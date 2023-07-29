from django import forms
from .models import foodItem

#creating form for adding data
class itemForm(forms.ModelForm):
    class Meta:
        model = foodItem
        fields = ['item_name', 'item_desc', 'item_price', 'item_image']
       