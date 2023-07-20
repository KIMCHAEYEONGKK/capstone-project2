from django.contrib import admin
from .models import Board
from django_summernote.admin import SummernoteModelAdmin


# Register your models here.
class BoardAdmin(admin.ModelAdmin):
    list_display = ('title',)


admin.site.register(Board, BoardAdmin)
