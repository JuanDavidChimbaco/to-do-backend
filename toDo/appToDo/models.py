from django.db import models
from django.contrib.auth import get_user_model

# Create your models here.

User = get_user_model()

class Tarea(models.Model):
    title = models.CharField(max_length=50)
    decription = models.TextField(max_length=250)
    completed = models.BooleanField()
    at_created = models.DateTimeField(auto_now_add=True)
    at_updated = models.DateTimeField(auto_now=True)
    usuario = models.ForeignKey(User, on_delete=models.CASCADE)
    
    def __str__(self):
        return self.title
