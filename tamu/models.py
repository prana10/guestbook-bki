from django.db import models
from django.utils.html import format_html
# Create your models here.
class Tamu(models.Model):
    name = models.CharField(null=False, max_length=255)
    origin_of_company = models.CharField(null=False, max_length=500)
    assurance = models.CharField(null=False, max_length=255)
    necessary = models.CharField(null=False, max_length=64)
    appointment_with = models.CharField(null=False, max_length=255)
    arrival_time = models.TimeField(auto_now_add=True, null=False)
    departure_time = models.TimeField(null=True)
    date = models.DateField(auto_now_add=True, null=False)
    photo = models.ImageField()
    def image_display(self):
        return format_html('<a href={0}><img href="{0}" src="{0}" width="48" height="48" /></a>'.format(self.photo.url))

    image_display.allow_tags = True
    image_display.short_description = 'Image'


class DataList(models.Model):
    name = models.CharField(null=False, max_length=255)
    divisi = models.CharField(null=False, max_length=255)

class Assurance(models.Model):
    type_assurance = models.CharField(null=False, max_length=64)