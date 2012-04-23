from django.db import models
from uzytkownicy.models import Uzytkownik

class Cwiczenie(models.Model) :
    nazwa = models.CharField(max_length=200)
    def __unicode__(self):
        return self.nazwa
    class Meta:
        verbose_name = 'Cwiczenie'
        verbose_name_plural = 'Cwicznia'
        
class Trening(models.Model):
    TYPY_TRENINGU = (
        (u'Test', u'Test'),
        (u'Normalny trening', u'Normalny trening'),        
    )
    uzytkownik = models.ForeignKey(Uzytkownik)                              
    typ = models.CharField(max_length=15, choices=TYPY_TRENINGU)
    cwiczenia = models.ManyToManyField(Cwiczenie, through='Pozycja')
    data = models.DateTimeField('Data treningu')
    czas = models.IntegerField()
    uwagi = models.TextField()
    def __unicode__(self):
        return unicode(self.data)
    class Meta:
        verbose_name = 'Trening'
        verbose_name_plural = 'Treningi'

class Pozycja(models.Model) :
    cwiczenie = models.ForeignKey(Cwiczenie, related_name='cwiczenie')
    trening = models.ForeignKey(Trening, related_name='trening')
    liczba_serii = models.IntegerField()
    obciazenia = models.CommaSeparatedIntegerField(max_length=30)
    ilosc_powtorzen = models.CommaSeparatedIntegerField(max_length=30)    
    def __unicode__(self):
        return self.cwiczenie.nazwa+" "+unicode(self.liczba_serii)+" serie"
    class Meta:
        verbose_name = 'Pozycja'
        verbose_name_plural = 'Pozycje'