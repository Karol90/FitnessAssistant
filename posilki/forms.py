from django import forms
from posilki.models import *
from django.forms.models import ModelForm

class ProduktForm(forms.ModelForm):
    class Meta:
        model = Produkt
        
class PosilekForm(forms.ModelForm):
    class Meta:
        model = Posilek

class PositionForm(forms.ModelForm):
    class Meta:
        model = Pozycja
        