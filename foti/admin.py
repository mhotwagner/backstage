from django.contrib import admin
from django.contrib.admin import ModelAdmin

from .models import Foto

class FotoAdmin(ModelAdmin):
    exclude = 'is_foto', 'is_scritto'

admin.site.register(Foto, FotoAdmin)
