from django.contrib import admin
from django.contrib.admin import ModelAdmin

from adminsortable2.admin import SortableAdminMixin

from .models import Scritto


class ScrittoAdmin(SortableAdminMixin, ModelAdmin):
    exclude = ['is_scritto', 'is_foto', 'opera_index',]

admin.site.register(Scritto, ScrittoAdmin)
