from django.db import models

from django.db import models

# Create your models here.

class BookList(models.Model):
    Id = models.AutoField(primary_key=True)
    Title = models.CharField(max_length=500)    
    Writer = models.CharField(max_length=2000)

class Login(models.Model):
    name = models.CharField(max_length=500)
    userName = models.CharField(primary_key=True,max_length=500)
    position = models.CharField(max_length=500)
    password = models.CharField(max_length=1000)
    salt = models.CharField(max_length=1000)
