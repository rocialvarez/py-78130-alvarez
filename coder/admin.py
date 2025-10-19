from django.contrib import admin
from coder.models import *


@admin.register(Estudiante)
class EstudianteAdmin(admin.ModelAdmin):
    list_display = ("nombre", "apellido", "nro_legajo", "fecha_de_nacimiento")
    list_display_links = ("nombre", "apellido")
    search_fields = ("nro_legajo",)
    list_filter = ("fecha_de_nacimiento",)
    ordering = ("apellido", "nombre", "nro_legajo")
    readonly_fields = ("nro_legajo",)