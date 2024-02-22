from django.db import models

# Create your models here.

class Appointment(models.Model):
    name=models.CharField(max_length=20)
    email=models.EmailField()
    mobile=models.BigIntegerField()
    dr=models.CharField(max_length=20)
    date=models.DateField()
    des=models.TextField()