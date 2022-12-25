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

class Session(models.Model):
    date = models.DateField('Session Date')
    session = models.TextField(max_length=250)

    character = models.ForeignKey(Character, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.session} on {self.date}"