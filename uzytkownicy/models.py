from django.db import models
from django.contrib.auth.models import User

class Uzytkownik(models.Model):
    user = models.OneToOneField(User)    
    imie = models.CharField(max_length=20, verbose_name="Imie")
    nazwisko = models.CharField(max_length=20, verbose_name="Naziwsko")
    data_urodzenia = models.DateField(null=True, verbose_name="Data urodzenia")
    kalorie_zap = models.IntegerField(verbose_name="Kalorie dziennie")
    bialko_zap = models.IntegerField(verbose_name="Bialko dziennie")
    weglow_zap = models.IntegerField(verbose_name="Weglowodany dziennie")
    tluszcze_zap = models.IntegerField(verbose_name="Tluszcze dziennie")
    
    
    def __unicode__(self):
        return self.user.username    
    
    class Meta:
        verbose_name = "Profil uzytkownika"
        verbose_name_plural = "Profile uzytkownikow"


