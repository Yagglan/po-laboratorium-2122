from django.contrib import admin

from .models import danie, skladniki, typ_dania

admin.site.register(typ_dania)
admin.site.register(danie)
admin.site.register(skladniki)

# Register your models here.
