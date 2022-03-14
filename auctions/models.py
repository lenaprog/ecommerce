from email.policy import default
from pickle import TRUE
from django.contrib.auth.models import AbstractUser
from django.db import models
from django.utils import timezone



class User(AbstractUser):
    pass

class Listing(models.Model):
    CATEGORY_CHOICES=[
        ('planets', 'Planets'),
        ('stars', 'Stars'),
        ('utensils', 'Utensils'),
        ('gargets', 'Gargets'),
    ]
    title = models.CharField(max_length=64)
    description = models.TextField()
    image = models.URLField(blank=True)
    starting_bid = models.DecimalField(max_digits=15, decimal_places=2)
    category = models.CharField(max_length=64, choices=CATEGORY_CHOICES, default=None)
    user = models.ForeignKey('User', on_delete=models.CASCADE, related_name="fulllist")
    date = models.DateTimeField(default=timezone.now)

class Bid(models.Model):
    listing = models.ForeignKey('Listing', on_delete=models.CASCADE, related_name="alllistedbids")
    amount = models.DecimalField(max_digits=15, decimal_places=2)
    user = models.ForeignKey('User', on_delete=models.CASCADE, related_name="alluserbids")
    date = models.DateTimeField()

class Comment(models.Model):
    user = models.ForeignKey('User', on_delete=models.CASCADE)
    text = models.CharField(max_length=150)
    listing = models.ForeignKey('Listing', on_delete=models.CASCADE)
    date = models.DateTimeField()

