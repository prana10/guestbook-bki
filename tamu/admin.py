from django.contrib import admin
from import_export.admin import ExportActionMixin

from tamu.models import DataList, Tamu, Assurance
# Register your models here.
class TamuAdmin(ExportActionMixin,admin.ModelAdmin):
    list_display = ('id', 'date', 'name', 'origin_of_company', 'assurance', 'necessary', 'appointment_with', 'arrival_time', 'departure_time', 'image_display')
    search_fields = ['id', 'date', 'name', 'origin_of_company', 'assurance', 'necessary', 'appointment_with', 'arrival_time', 'departure_time']
    list_per_page = 5
    list_filter = ('date',)

admin.site.register(Tamu, TamuAdmin)

class DataListAdmin(ExportActionMixin,admin.ModelAdmin):
    list_display = ('id', 'name', 'divisi')
    search_fields = ('id', 'name', 'divisi')
    list_per_page = 5

admin.site.register(DataList, DataListAdmin)

@admin.register(Assurance)
class AssuranceDataList(admin.ModelAdmin):
    list_display = ('id', 'type_assurance')
    search_fields = ['id', 'type_assurance']
    list_per_page = 5