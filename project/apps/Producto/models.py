from django.db import models



class celular (models.Model):
    nombre = models.CharField(max_length=50, null=False)
    descripcion=models.TextField()
    precio = models.PositiveIntegerField(null=False)
    fecha_ingreso = models.DateField(null=False)
    imagen = models.CharField(max_length=1000)
    
    def __str__(self):
        return f"{self.nombre} {self.descripcion} - ${self.precio}. Categoría: {self.categoria}. Ingresado: {self.fecha_ingreso}'"
    