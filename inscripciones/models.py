from main.models import Curso
from datetime import datetime
from django.contrib.auth.models import User
from django.db import models
from django.db.models.fields import DateField

# Create your models here.

class Incripciones(models.Model):
    estudiante = models.ForeignKey(User,on_delete=models.CASCADE)
    fecha_inscripcion = models.DateField()
        "Fecha de publicación", default= datetime.now())
    curso_Curso = models.ForeignKey(Curso, on_delete=models.CASCADE)
    costo_total = models.DecimalField(max_digits=3, decimal_places=2, default=0)

def _str_(self):
    return self.estudiante
