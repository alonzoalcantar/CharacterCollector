from django.db import models
from django.urls import reverse
# Create your models here.

class Character(models.Model):
    name = models.CharField(max_length=100)
    race = models.CharField(max_length=100)
    background = models.CharField(max_length=100)
    level = models.IntegerField()
    style = models.CharField(max_length=100)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse("detail", kwargs={"character_id": self.id})
    
class Item(models.Model):
    name = models.CharField(max_length=100)
    notes = models.TextField(max_length=250)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse("itemdetail", kwargs={"item_id": self.id})