from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import pre_save
from django.dispatch import receiver
from .ai_logic import analyze_review_sentiment

class Category(models.Model):
    name = models.CharField(max_length=100)
    def __str__(self): return self.name

class Product(models.Model):
    name = models.CharField(max_length=200)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    description = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    stock = models.IntegerField()
    # New Fields
    image = models.ImageField(upload_to='products/') 
    specifications = models.JSONField(default=dict, blank=True) # The NoSQL Flex!

    def __str__(self): return self.name

class Review(models.Model):
    # In MongoDB, we use CharField for IDs to avoid join errors
    product_name = models.CharField(max_length=200) 
    user_name = models.CharField(max_length=100)
    comment = models.TextField()
    sentiment = models.CharField(max_length=20, blank=True)

    def __str__(self): return f"{self.user_name} - {self.product_name}"

@receiver(pre_save, sender=Review)
def apply_ai_sentiment(sender, instance, **kwargs):
    if not instance.sentiment:
        instance.sentiment = analyze_review_sentiment(instance.comment)