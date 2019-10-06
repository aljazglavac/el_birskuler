from django.contrib import admin

from .models import Uporabniki, Turnir


class UporabnikiAdmin(admin.ModelAdmin):
    fields = ['ime', 'odsek', 'slika', 'tocke', 'turnir']


class TurnirAdmin(admin.ModelAdmin):
    fields = ['ime', 'datum', 'status', 'prvi', 'drugi', 'tretji']
    readonly_fields = ['prvi', 'drugi', 'tretji']
    change_form_template = 'briskula/custom_change_form.html'

    def save_model(self, request, obj, form, change):
        if '_end' in request.POST:
            uporabniki = Uporabniki.objects.filter(turnir=obj)
            for u, f in zip(uporabniki, ('prvi', 'drugi', 'tretji')):
                setattr(obj, f, u.ime)
                obj.status = False
                obj.save()
        else:
            super(TurnirAdmin, self).save_model(request, obj, form, change)


admin.site.register(Uporabniki, UporabnikiAdmin)
admin.site.register(Turnir, TurnirAdmin)
