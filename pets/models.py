from django.db import models

# Create your models here.

# lets create our first model. A turtle!
# Create new model class that inherits from models.Model

# Model are singular uppercase
class Turtle(models.Model):
    # define the fields in the model
    # define string field of 100 char max
    name = models.CharField(max_length=100)
    # define an age that is an integer (whole number)
    age = models.IntegerField()
    
# Tell DB model exsists, run a migration
# upon completion, you can initialize the migrate (pack things up
# python manage.py migrate

# From there, you can initiate the migration via
# python manage.py make migrations