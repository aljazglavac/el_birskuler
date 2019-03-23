from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Uporabniki, Turnir
from .forms import UporabnikiForm
from django.conf import settings


def index(request):
    uporabniki = Uporabniki.objects.all()
    top3 = uporabniki[:3]
    form = UporabnikiForm()
    context = {
        'ranking': uporabniki,
        'form': form,
        'media_url': settings.MEDIA_URL,
        'top3': top3
    }
    return render(request, 'briskula/index.html', context)


def shrani_uporabnika(request):
    if request.method == 'POST':
        UporabnikiForm(request.POST, request.FILES).save()
    return redirect('/')


def najdi_udelezence(request, turnir_id):
    turnir = Turnir.objects.get(pk=turnir_id)
    uporabniki = Uporabniki.objects.filter(turnir=turnir)

    context = {
        'udelezenci': uporabniki,
        'turnir' : turnir,
    }

    return render(request, 'briskula/info.html', context)