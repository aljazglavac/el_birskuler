from django.urls import path

from .views import shrani_uporabnika as su

urlpatterns = [
    path('shrani', su, name='shrani'),
]
