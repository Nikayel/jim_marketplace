from django import forms

from .models import Item

INPUT_CLASSES = "w-full py-4 px-6 rounded-xl border"
class NewItemForm(forms.ModelForm):
    class Meta:
        model = Item
        fields = ('catagory', 'name', 'description', 'price', 'image')
        widgets = {
            'catagory': forms.Select(attrs={'class': 'w-full py-4 px-6 rounded-xl border'}),
            'name': forms.TextInput(attrs={'class': 'w-full py-4 px-6 rounded-xl border'}),
            'price': forms.TextInput(attrs={'class': 'w-full py-4 px-6 rounded-xl border'}),
            'description': forms.Textarea(attrs={'class': INPUT_CLASSES}),
        }

class EditItemForm(forms.ModelForm):
    class Meta:
        model = Item
        fields = ('catagory', 'name', 'description', 'price', 'image', 'is_sold')
        widgets = {
            'name': forms.TextInput(attrs={'class': 'w-full py-4 px-6 rounded-xl border'}),
            'price': forms.TextInput(attrs={'class': 'w-full py-4 px-6 rounded-xl border'}),
            'description': forms.Textarea(attrs={'class': INPUT_CLASSES}),
        }