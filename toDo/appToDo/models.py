from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.

class Tarea(models.Model):
    title = models.CharField(max_length=50)
    decription = models.TextField(max_length=250)
    completed = models.BooleanField()
    
class User(AbstractUser):
    fotoPerfil = models.ImageField(upload_to=None, height_field=None, width_field=None, max_length=None, null=True, blank=True) 
    