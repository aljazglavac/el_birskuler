import os
from django.db import models


def get_image_path(instance, filename):
    return os.path.join('photos', str(instance.id), filename)

class Uporabniki(models.Model):
    ime = models.CharField(max_length=30)
    odsek = models.CharField(max_length=2)
    slike = ImageField(upload_to=get_image_path, blank=True, null=True)
    tocke = models.IntegerField()

    def __str__(self):
        return '{}, {}'.format(self.ime, self.odsek)

    def pridobi_tocke(self):
        return self.tocke

    class meta:
        ordering = ['tocke']
