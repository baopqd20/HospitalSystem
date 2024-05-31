from django.db import models

# Create your models here.
class FullName(models.Model):
    fname = models.CharField(max_length=200,null=True)
    lname = models.CharField(max_length=200,null=True)

    def __str__(self):
        return f"{self.fname} {self.lname}"

class Address(models.Model):
    provice = models.CharField(max_length=200,null=True)
    district = models.CharField(max_length=200,null=True)
    ward = models.CharField(max_length=200,null=True)
    detail = models.CharField(max_length=200,null=True)

    def __str__(self):
        return f"{self.detail}, {self.ward}, {self.district}, {self.provice}"

class Patient(models.Model):
    fullName = models.ForeignKey(FullName,on_delete=models.SET_NULL,null=True)
    cardId = models.CharField(max_length=200,null=True)
    gender = models.CharField(max_length=20,null=True)
    dob = models.DateField()
    address = models.ForeignKey(Address,on_delete=models.SET_NULL,null=True)
    contact = models.CharField(max_length=200,null=True)

