from django.db import models

# Create your models here.

# Create a Cat model

# Singular uppercase
class Cat(models.Model):
    name = models.CharField(max_length=100)
    breed = models.CharField(max_length=100)
    age = models.IntegerField()
    sex = models.CharField(max_length=100)
    price = models.IntegerField()
    