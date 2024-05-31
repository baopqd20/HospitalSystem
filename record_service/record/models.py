from django.db import models

class Record(models.Model):
    idPatient = models.IntegerField()
    idDoctor = models.IntegerField()
    result = models.CharField(max_length=200,null=False)
    medicine = models.CharField(max_length=200,null=True)
    boarding = models.CharField(max_length=200,null=True)
    note = models.CharField(max_length=200,null=True)
    createdDay = models.DateField(auto_now_add=True)
    reSchedule = models.DateField()
    fee = models.IntegerField()

    age = models.IntegerField()
    patientName = models.CharField(max_length=200,null=False)
    patientContact = models.CharField(max_length=200,null=True)

    doctorName = models.CharField(max_length=200, null=False)
    doctorContact = models.CharField(max_length=200,null=True)
    


