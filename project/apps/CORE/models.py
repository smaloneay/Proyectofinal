from django.db import models

class Estudiante(models.Model):
    nombre = models.CharField(max_length=100)
    edad = models.IntegerField()
    direccion = models.CharField(max_length=200)

class Profesor(models.Model):
    nombre = models.CharField(max_length=100)
    especialidad = models.CharField(max_length=100)
    salario = models.DecimalField(max_digits=8, decimal_places=2)

class Curso(models.Model):
    nombre = models.CharField(max_length=100)
    duracion = models.IntegerField()
    profesor = models.ForeignKey(Profesor, on_delete=models.CASCADE)
    estudiantes = models.ManyToManyField(Estudiante)