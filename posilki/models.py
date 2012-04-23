from django.db import models
from uzytkownicy.models import Uzytkownik
    
class Kategoria(models.Model):
    nazwa = models.CharField(max_length=200)
    def __unicode__(self):
        return self.nazwa
    class Meta:
        verbose_name = 'Kategoria'
        verbose_name_plural = 'Kategorie'
    
class Produkt(models.Model):
    nazwa = models.CharField(max_length=200) 
    kategoria = models.ForeignKey(Kategoria)
    kalorie = models.IntegerField(null=True, blank=True)
    bialko = models.IntegerField()
    tluszcz = models.IntegerField()
    weglowodany = models.IntegerField()
     
    #obrazek moze jeszcze
    def __unicode__(self):
        return self.nazwa    
    class Meta:
        verbose_name = 'Produkt'
        verbose_name_plural = 'Produkty'   

#czyli produkt + jego ilosc        
        
class Posilek(models.Model):
    TYPY_POSILKU = (
        (u'Sniadanie', u'Sniadanie'),
        (u'Drugie sniadanie', u'Drugie sniadanie'),
        (u'Obiad', u'Obiad'),
        (u'Kolacja', u'Kolacja'),
        (u'Przekaska', u'Przekaska'),
    )
    # nazwa = models.CharField(max_length=200)
    uzytkownik = models.ForeignKey(Uzytkownik)
    typ =     models.CharField(max_length=20, choices=TYPY_POSILKU)
    data = models.DateTimeField('Data jedzenenia')
    pozycje= models.ManyToManyField(Produkt, through='Pozycja')
    uwagi = models.TextField()    
    def __unicode__(self):
        return self.typ + " " + unicode(self.data)
    class Meta:
        verbose_name = 'Posilek'
        verbose_name_plural = 'Posilki'
        
class Pozycja(models.Model):
    produkt = models.ForeignKey(Produkt, related_name="produkt")
    posilek = models.ForeignKey(Posilek, related_name="posilek")
    ilosc = models.IntegerField()
    def __unicode__(self):
        return self.produkt.nazwa+" " + unicode(self.ilosc)
    class Meta:
        verbose_name_plural = 'Pozycje'