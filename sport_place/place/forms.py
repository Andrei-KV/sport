from django import forms
from .models import *

class AddPlaceForm(forms.Form):
    title = forms.CharField(
        max_length=255, 
        label='Place title', 
        widget=forms.TextInput(attrs={'class': 'form-input'}),
        )
    slug = forms.SlugField(
        max_length=255, 
        label='URL', 
        widget=forms.TextInput(attrs={'class': 'form-input'}),
        )
    address = forms.CharField(
        widget=forms.Textarea(attrs={'cols': 50, 'rows': 4}), 
        label='Place address',
        )
    is_published = forms.BooleanField(label='Published', initial=True)
    sport_category = forms.ModelChoiceField(
        queryset=SportCategory.objects.all(), 
        label='Sport category',
        empty_label='Without category',
        widget=forms.Select(attrs={'class': 'form-input'}))

