from django import forms
from posilki.models import *
from django.forms.models import ModelForm

class ProduktForm(forms.ModelForm):
    class Meta:
        model = Produkt
        
class PosilekForm(forms.ModelForm):
    class Meta:
        model = Posilek
        exclude = ('uzytkownik','pozycje')

class PositionForm(forms.ModelForm):
    class Meta:
        model = Pozycja
        exclude = ('posilek',)
        