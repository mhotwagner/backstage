from django.contrib import admin

from solo.admin import SingletonModelAdmin

from .models import Profile

admin.site.register(Profile, SingletonModelAdmin)

