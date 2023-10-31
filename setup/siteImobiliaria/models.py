from django.db import models


class Imoveis(models.Model):
    address = models.TextField()
    status =  models.TextField()
    area = models.TextField()
    bedrooms = models.TextField()
    bathrooms = models.TextField()
    floor = models.TextField()
    floor = models.TextField()
    parking = models.TextField()
    value = models.TextField()
    type = models.TextField()
    path = models.TextField()
    
    def __str__(self):
        return self.address.status.area.bedrooms.bathrooms.floor.parking.value.type.path

class Message(models.Model):
    name = models.TextField()
    email =  models.TextField()
    subject = models.IntegerField()
    message= models.TextField()
    
    
    def __str__(self):
        return self.message

