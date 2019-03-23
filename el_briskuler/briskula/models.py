import datetime
import os
from django.db import models

ODSEK = (('E9', 'E9'), )


class Turnir(models.Model):
    ime = models.CharField(max_length=30)
    datum = models.DateField(default=datetime.date.today)
    status = models.BooleanField(default=True)
    prvi = models.CharField(max_length=30, null=True)
    drugi = models.CharField(max_length=30, null=True)
    tretji = models.CharField(max_length=30, null=True)

    def __str__(self):
        return self.ime

    def razvrstitev(self):
        return [self.prvi, self.drugi, self.tretji]

    class Meta:
        ordering = ['-datum']
        verbose_name_plural = 'Turnir'


class Uporabniki(models.Model):
    ime = models.CharField(max_length=30)
    odsek = models.CharField(max_length=2, choices=ODSEK)
    slika = models.ImageField(upload_to='', default=None)
    tocke = models.PositiveIntegerField(null=True, default=0)
    turnir = models.ForeignKey(Turnir, on_delete=models.CASCADE, null=True)

    def __str__(self):
        return '{}, {}'.format(self.ime, self.odsek)

    def pridobi_tocke(self):
        return self.tocke

    class Meta:
        ordering = ['-tocke']
        verbose_name_plural = 'Uporabniki'
