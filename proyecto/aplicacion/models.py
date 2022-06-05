from django.db import models

# Create your models here.

class Cliente(models.Model):
    nombre=models.CharField(max_length=20)
    apellido=models.CharField(max_length=20)
    def __str__(self):
        return (self.nombre+' '+self.apellido)
      