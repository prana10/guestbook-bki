from django.contrib import admin
from import_export.admin import ExportActionMixin

from tamu.models import Tamu
# Register your models here.
class TamuAdmin(ExportActionMixin,admin.ModelAdmin):
    list_tamu = ('id', 'date', 'name', 'origin of company', 'assurance', 'necessary', 'appointment with', 'arrival time', 'departure time', 'photo')

admin.site.register(Tamu, TamuAdmin)
