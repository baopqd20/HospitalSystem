from django.db import models
from django.utils import timezone
# Create your models here.

class Appointment(models.Model):
    idPatient = models.CharField(max_length=20)
    idDoctor = models.CharField(max_length=20)
    date = models.DateField()
    idRoom = models.CharField(max_length = 20)
    status = models.CharField(max_length = 20)
    note = models.CharField(max_length=500)
    createdDate = models.DateField(default=timezone.now)

    patientName = models.CharField(max_length=50)
    patientContact = models.CharField(max_length=50)
    doctorName = models.CharField(max_length=50)
    doctorContact = models.CharField(max_length=50)
    roomNumber = models.CharField(max_length=50)
    buildingName = models.CharField(max_length=50)