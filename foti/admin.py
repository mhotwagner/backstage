from django.contrib import admin
from django.contrib.admin import ModelAdmin

from adminsortable2.admin import SortableAdminMixin

from .models import Foto


class FotoAdmin(SortableAdminMixin, ModelAdmin):
    exclude = ['is_foto', 'is_scritto']

admin.site.register(Foto, FotoAdmin)
