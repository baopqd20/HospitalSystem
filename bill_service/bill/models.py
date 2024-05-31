from django.db import models

# Create your models here.
class Bill(models.Model):
    idPayment = models.IntegerField()
    idEmployee = models.IntegerField()
    recipientName = models.CharField(max_length=100,null=False)
    createdDay = models.DateField(auto_now_add=True)

    medicine = models.CharField(max_length=100,null=True)
    fee = models.IntegerField()
    bedFee = models.IntegerField()
    paymentDay = models.DateField()
    contact = models.CharField(max_length=200,null=True)
    total = models.IntegerField()


