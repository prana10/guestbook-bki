from django.contrib import admin
from import_export.admin import ExportActionMixin

from tamu.models import DataList, Tamu
# Register your models here.
class TamuAdmin(ExportActionMixin,admin.ModelAdmin):
    list_display = ('id', 'date', 'name', 'origin_of_company', 'assurance', 'necessary', 'appointment_with', 'arrival_time', 'departure_time', 'photo')
    search_fields = ['id', 'date', 'name', 'origin_of_company', 'assurance', 'necessary', 'appointment_with', 'arrival_time', 'departure_time', 'photo']

admin.site.register(Tamu, TamuAdmin)

class DataListAdmin(ExportActionMixin,admin.ModelAdmin):
    list_display = ('id', 'name', 'divisi')
    search_fields = ('id', 'name', 'divisi')

admin.site.register(DataList, DataListAdmin)
