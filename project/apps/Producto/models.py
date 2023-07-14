from django.db import models



class curso (models.Model):
    nombre = models.CharField(max_length=50)
    descripcion=models.models.TextField()

    def __str__(self):
        return f"{self.nombre} {self.descripcion}"