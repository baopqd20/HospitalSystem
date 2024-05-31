from django.db import models

# Create your models here.
class Fullname(models.Model):
    fname = models.CharField(max_length=20)
    lname = models.CharField(max_length=20)

    def __str__(self):
        return '%s %s' % (self.fname, self.lname)
    
class Department(models.Model):
    name = models.CharField(max_length=20)
    specialization = models.CharField(max_length = 30)
    departmentId = models.CharField(max_length = 30)
    description = models.CharField(max_length = 1000)

    def __str__(self):
        return '%s' % (self.name)


class Address(models.Model):
    provice = models.CharField(max_length=20)
    district = models.CharField(max_length = 20)
    ward = models.CharField(max_length = 20)
    details = models.CharField(max_length = 20)

    def __str__ (self):
        return '%s, %s, %s, %s' % (self.details, self.ward, self.district, self.provice)
class Doctor(models.Model):
    fullname = models.ForeignKey(Fullname, on_delete=models.CASCADE)
    gender = models.CharField(max_length=10)
    address = models.ForeignKey(Address, on_delete=models.CASCADE)
    cardId = models.CharField(max_length=14)
    dob = models.DateField()
    department = models.ForeignKey(Department, on_delete=models.CASCADE)
    email = models.CharField(max_length=30)

    def __str__(self):
        return '%s %s %s %s %s %s %s' % (self.fullname, self.gender, self.address, self.cardId, self.dob, self.department, self.email)




    
