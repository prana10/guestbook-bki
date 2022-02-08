from django.db import models

# Create your models here.
class Tamu(models.Model):
    name = models.TextField(null=False)
    origin_of_company = models.TextField(null=False)
    assurance = models.CharField(null=False, max_length=255)
    necessary = models.TextField(null=False)
    appointment_with = models.TextField(null=False)
    arrival_time = models.TimeField(auto_now_add=True, null=False)
    departure_time = models.TimeField(null=True)
    date = models.DateField(auto_now_add=True, null=False)
    photo = models.TextField(null=False)