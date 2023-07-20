from django.contrib import admin
from .models import Setting

# Register your models here.


class SettingAdmin(admin.ModelAdmin):
    list_displays = ('weight', 'fat', 'muscle', 'target_weight')


admin.site.register(Setting, SettingAdmin)