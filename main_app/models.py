from django.db import models

# Create your models here.

class Character(models.Model):
    name = models.CharField(max_length=100)
    race = models.CharField(max_length=100)
    background = models.CharField(max_length=100)
    level = models.IntegerField()
    style = models.CharField(max_length=100)
