from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Uporabniki, Turnir
from .forms import UporabnikiForm
from django.conf import settings
from django.db.models import Sum


def index(request):
    form = UporabnikiForm()
    t = Turnir.objects.all()
    prih = t.filter(status=True)
    pret = t.filter(status=False)
    zadnji = t.first()
    raz = Uporabniki.objects \
            .values('ime') \
            .annotate(tocke=Sum('tocke'))
    context = {
        'form': form,
        'media_url': settings.MEDIA_URL,
        'prihajajoci': prih,
        'pretekli': pret,
        'zadnji': zadnji,
        'razvrstitev': raz,
    }
    return render(request, 'briskula/index.html', context)


def shrani_uporabnika(request):
    if request.method == 'POST':
        UporabnikiForm(request.POST, request.FILES).save()
    return redirect('/')
