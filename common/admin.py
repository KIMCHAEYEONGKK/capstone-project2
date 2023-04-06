from django.contrib import admin
from .models import Common
from .forms import UserChangeForm, UserCreateForm
from django.contrib.auth.models import Group
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin


# class UserAdmin(BaseUserAdmin):
#     form = UserChangeForm
#     add_form = UserCreateForm
#
#     list_display = ('username',)
#     list_filter = ()
#     fieldsets = ()
#     search_fields = ('username','name',"age","tall","gender","exercise")
#     filter_horizontal = ()
#

admin.site.register(Common)

