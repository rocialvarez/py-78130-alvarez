from django.db import models

# Create your models here. nota del profe: donde vamos a ir creando las tablas

class Estudiante(models.Model):
    nombre = models.CharField(max_length=100)
    apellido = models.CharField(max_length=100)
    email = models.EmailField()
    nro_legajo = models.IntegerField(unique=True)
    fecha_de_nacimiento = models.DateField(null=True)
    def __str__(self):
        return f"Estudiante: {self.nombre} - Nro Legajo: {self.nro_legajo}"
    
    # si quiero editar puedo hacerlo, guardar, y ejecutar python manage.py makemigrations de vuelta
