from django.db import models
from datetime import datetime

# Create your models here.

class Curso(models.Model):
    curso_titulo = models.CharField(max_length= 200)
    curso_contenido = models.TextField()
    curso_publicado = models.DateTimeField(
        "Fecha de publicación", default= datetime.now())
    curso_costo = models.DecimalField(max_digits=5, decimal_places=2)

def _str_(self):
    return self.curso_titulo