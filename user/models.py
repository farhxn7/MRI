from django.db import models

# Create your models here.
class UserRegister(models.Model):
    name=models.CharField(max_length=100)
    username =models.CharField(max_length=100)
    password = models.CharField(max_length=100)
    email = models.EmailField()
    moblie_no = models.CharField(max_length=100)
    address = models.CharField(max_length=100)
    locality = models.CharField(max_length=100)
    city = models.CharField(max_length=100)
    state = models.CharField(max_length=100)
    status = models.CharField(max_length=100)
    
    def __str__(self):
        return self.Name
    