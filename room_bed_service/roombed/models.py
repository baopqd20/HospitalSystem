from django.db import models

# Create your models here.

class Room(models.Model):
    floor = models.CharField(max_length = 10)
    note = models.CharField(max_length = 500)
    type = models.CharField(max_length = 10)
    buildingName = models.CharField(max_length=10)
    roomNumber = models.CharField(max_length=10)

    def __str__(self):
        return f'{self.roomNumber} {self.buildingName}'

class Bed(models.Model):
    room = models.ForeignKey(Room, on_delete = models.CASCADE)
    note = models.CharField(max_length= 500)
    price = models.CharField(max_length = 100)
    bedNumber = models.CharField(max_length=1000)