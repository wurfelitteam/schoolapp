from django.db import models

# Create your models here.

class student(models.Model):
    name = models.CharField(max_length=200)
    fathername = models.CharField(max_length=1000)
    classname = models.IntegerField()
    contact = models.CharField(max_length=100)
