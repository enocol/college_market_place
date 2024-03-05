from django.db import models

# Create your models here.
class Market(models.Model):
    title = models.CharField(max_length=100)
    image = models.ImageField('image', default='placeholder')