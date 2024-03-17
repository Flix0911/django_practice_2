from django.db import models

# Create your models here.

# Create a dog model

# Singular uppercase
class Dog(models.Model):
    # define the field in the mode
    name = models.CharField(max_length=100)
    breed = models.CharField(max_length=100)
    age = models.IntegerField()
    color = models.CharField(max_length=100)