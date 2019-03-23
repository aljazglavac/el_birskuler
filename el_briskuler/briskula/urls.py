from django.urls import path

from .views import shrani_uporabnika, najdi_udelezence

urlpatterns = [
    path('shrani', shrani_uporabnika, name='shrani'),
    path('turnir/<int:turnir_id>/info', najdi_udelezence, name='turnir'),
]
