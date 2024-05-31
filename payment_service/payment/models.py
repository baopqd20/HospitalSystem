from django.db import models
from django.utils import timezone
# Create your models here.
class Payment(models.Model):
    idRecord = models.CharField(max_length=20)
    patientName = models.CharField(max_length =40)
    total = models.CharField(max_length=20)
    medicine = models.CharField(max_length=500)
    fee = models.CharField(max_length = 20)
    createdDate = models.DateField(default=timezone.now)
    status = models.CharField(max_length=50)
    contact = models.CharField(max_length = 20)
    idPatient = models.CharField(max_length = 20)
    bedFee = models.CharField(max_length=20)