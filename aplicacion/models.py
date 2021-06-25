from django.db import models
from django.utils import timezone

# Create your models here.

class Animal(models.Model):
  autor = models.ForeignKey('auth.User', on_delete=models.CASCADE)
  nombre = models.CharField(max_length=200)
  especie = models.CharField(max_length=200)
  receta_medica = models.TextField()
  fecha_emision = models.DateTimeField(default=timezone.now)
  precio_consulta = models.CharField(max_length=6)

  def publish(self):
    self.published_date = timezone.now()
    self.save()

  def __str__(self):
    return self.nombre

