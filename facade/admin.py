from django.contrib import admin

from solo.admin import SingletonModelAdmin

from foti.models import Foto
from opere.models import Opera
from scritti.models import Scritto
from .models import Profile


# class OperaInline(admin.StackedInline):
#     model = Opera
#
#
# class ScrittoInline(admin.StackedInline):
#     model = Scritto
#
#
# class FotoInline(admin.StackedInline):
#     model = Foto
#
#
# class ProfileAdmin(SingletonModelAdmin):
#     inline = [
#         OperaInline,
#         ScrittoInline,
#         FotoInline,
#     ]


admin.site.register(Profile, SingletonModelAdmin)
