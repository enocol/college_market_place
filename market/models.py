from django.db import models
from django.contrib.auth.models import User
from cloudinary.models import CloudinaryField

# Create your models here.
class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)

    
class Product(models.Model):
    CATEGORY_CHOICES = [('Female item', 'FM'), ('MALE item', 'MA')]
    CONDITION_CHOICES = [('New', 'NEW'),('Used', 'USED')]
    title = models.CharField(max_length=100)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    category = models.CharField(max_length=20, choices=CATEGORY_CHOICES)
    condition = models.CharField(max_length=20, choices=CONDITION_CHOICES)
    description = models.TextField()
    image = CloudinaryField('image', default='placeholder')
    created_at = models.DateTimeField(auto_now_add=True)
    is_sold = models.BooleanField(default=False)
