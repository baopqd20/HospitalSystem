from django.db import models

# Create your models here.
class Medicine(models.Model):
    name = models.CharField(max_length=200,null=True)
    price = models.IntegerField()
    brand = models.CharField(max_length=200,null=True)
    expdate = models.DateField()
    note = models.CharField(max_length=200,null=True)
    status = models.CharField(max_length=200,null=True)

    def __str__(self):
        return f"{self.name}"