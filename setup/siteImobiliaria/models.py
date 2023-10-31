from django.db import models

class Imovel(models.Model):
    address = models.CharField(max_length=255)
    status = models.CharField(max_length=20)
    area = models.DecimalField(max_digits=10, decimal_places=2)
    bedrooms = models.IntegerField()
    bathrooms = models.IntegerField()
    floor = models.IntegerField()
    parking = models.IntegerField()
    value = models.DecimalField(max_digits=15, decimal_places=2)
    type = models.CharField(max_length=20)
    path = models.CharField(max_length=255)
    
class Message(models.Model):
    name = models.CharField(max_length=255)
    email = models.CharField(max_length=255)
    subject = models.CharField(max_length=255)
    message = models.TextField()  # Use TextField para armazenar mensagens mais longas
