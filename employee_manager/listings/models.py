from django.db import models
from django.forms import IntegerField

# Create your models here.
class Employee(models.Model):
    name = models.fields.CharField(max_length=100)
    surname = models.fields.CharField(max_length=100)
    departement = models.fields.CharField(max_length=100)
    age = IntegerField()