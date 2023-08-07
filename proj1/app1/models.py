from django.db import models

# Create your models here.

class App(models.Model):
    firstname = models.CharField(max_length=300)
    lastname = models.CharField(max_length=350)

    
