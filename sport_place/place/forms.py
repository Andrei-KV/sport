from django import forms
from django.forms import ValidationError
from .models import *

class AddPlaceForm(forms.ModelForm):
    # title = forms.CharField(
    #     max_length=255, 
    #     label='Place title', 
    #     widget=forms.TextInput(attrs={'class': 'form-input'}),
    #     )
    # slug = forms.SlugField(
    #     max_length=255, 
    #     label='URL', 
    #     widget=forms.TextInput(attrs={'class': 'form-input'}),
    #     )
    # address = forms.CharField(
    #     widget=forms.Textarea(attrs={'cols': 50, 'rows': 4}), 
    #     label='Place address',
    #     )
    # is_published = forms.BooleanField(label='Published', initial=True)
    # sport_category = forms.ModelChoiceField(
    #     queryset=SportCategory.objects.all(), 
    #     label='Sport category',
    #     empty_label='Without category',
    #     widget=forms.Select(attrs={'class': 'form-input'}))
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['sport_category'].empty_label = "Category didn't choose"

    class Meta:
        model = PlaceTitle
        fields = ['title', 'slug', 'address', 'is_published', 'sport_category']
        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-input'}),
            'address': forms.Textarea(attrs={'cols': 50, 'rows': 4}),
            'sport_category': forms.Select(attrs={'class': 'form-input'}),
        }
        
class AddDescriptionForm(forms.ModelForm):
    
    class Meta:
        model = Description
        fields = ['description', 'photo', 'placetitle']
    
    def clean_description(self):
        description = self.cleaned_data['description']
        maxlen = 500
        if len(description) > maxlen:
            raise ValidationError(f'Too long text (max {maxlen} symbols)')
        return description
