from django.db import models

# Create your models here.


class Personaje(models.Model):
    '''Carreras de cada sede'''
    nombre = models.CharField(max_length=300)
    nivel = models.IntegerField(default=1)

    def __str__(self):
        return f"{self.nombre} - {self.nivel}"
