from django.db import models

# Create your models here.

# Create a Bird model

# Singular uppercase

class Bird(models.Model):
    name = models.CharField(max_length=100)
    breed = models.CharField(max_length=100)
    age = models.IntegerField()
    size = models.CharField(max_length=100)
    color = models.CharField(max_length=100)
    