from django import forms
from django.contrib.auth.models import User
from django.forms.widgets import PasswordInput
from django.forms.models import ModelForm
from uzytkownicy.models import Uzytkownik

class RegisterForm(ModelForm):
    username = forms.CharField(label="Nazwa uzytkownika")
    password = forms.CharField(widget=PasswordInput, label='Haslo')
    confirm_password = forms.CharField(widget=PasswordInput, label='Potwierdz haslo')
    email = forms.EmailField(label='Email')
    
    class Meta:
        model = Uzytkownik
        fields = ('username', 'password', 'confirm_password', 'email', 'imie', 'nazwisko', 'data_urodzenia','kalorie_zap','bialko_zap','weglow_zap','tluszcze_zap',) 
        #
        
    def clean_password(self):
        if self.data['password'] != self.data['confirm_password']:
            raise forms.ValidationError('Hasla nie sa identyczne')
        return self.data['password']

class UserForm(ModelForm):
    class Meta:
        password = forms.CharField(widget=PasswordInput, label='Haslo')        
        model = User        
        fields = ('username', 'email', 'password',)

class EditProfileForm(ModelForm):
    #21.27 dzialajaca wersja
    #username = forms.CharField(label="Nazwa uzytkownika")
    #password = forms.CharField(widget=PasswordInput, label='Haslo')
    #confirm_password = forms.CharField(widget=PasswordInput, label='Potwierdz haslo')
    #email = forms.EmailField(label='Email')    
    class Meta:
        model = Uzytkownik        
        fields = ('imie', 'nazwisko', 'data_urodzenia','kalorie_zap','bialko_zap','weglow_zap','tluszcze_zap',) 
    def clean_password(self):
        if self.data['password'] != self.data['confirm_password']:
            raise forms.ValidationError('Hasla nie sa identyczne')
        return self.data['password']    
   
    
    