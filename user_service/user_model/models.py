from django.db import models

class UserRegistration(models.Model):
    fname = models.CharField(max_length=50)
    lname = models.CharField(max_length=50)
    email = models.CharField(max_length=50)
    mobile = models.CharField(max_length=12)
    password = models.CharField(max_length=50)
    address = models.CharField(max_length=200)
    
    def __str__(self):
        return f'{self.fname} {self.lname} {self.email} {self.mobile} {self.password} {self.address}'
