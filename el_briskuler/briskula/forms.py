from django.forms import ModelForm
from .models import Uporabniki, Turnir


class UporabnikiForm(ModelForm):
    def __init__(self, *args, **kwargs):
        super(UporabnikiForm, self).__init__(*args, **kwargs)
        self.fields['turnir'].queryset = Turnir.objects.filter(status=True)

    class Meta:
        model = Uporabniki
        fields = ['ime', 'odsek', 'slika', 'turnir']
