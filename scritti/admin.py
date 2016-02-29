from django.contrib import admin
from django.contrib.admin import ModelAdmin

from .models import Scritto

class ScrittoAdmin(ModelAdmin):
    exclude = 'is_scritto', 'is_foto'

admin.site.register(Scritto, ScrittoAdmin)
