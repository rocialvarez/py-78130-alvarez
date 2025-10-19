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

class Grupo(models.Model):
    nombre = models.CharField(max_length=100)
    pais_origen = models.CharField(max_length=50)
    debut = models.DateField()

    def __str__(self):
        return f"{self.nombre} ({self.pais_origen})"

class Album(models.Model):
    titulo = models.CharField(max_length=100)
    grupo = models.ForeignKey(Grupo, on_delete=models.CASCADE)
    fecha_lanzamiento = models.DateField()
    precio = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return f"{self.titulo} - {self.grupo.nombre}"