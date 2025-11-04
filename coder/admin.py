from django.contrib import admin
from coder.models import *


@admin.register(Cliente)
class ClienteAdmin(admin.ModelAdmin):
    list_display = ("nombre", "apellido", "email", "fecha_de_nacimiento")
    list_display_links = ("nombre", "apellido")
    search_fields = ("nombre", "apellido", "email")
    list_filter = ("fecha_de_nacimiento",)
    ordering = ("apellido", "nombre")

@admin.register(Grupo)
class GrupoAdmin(admin.ModelAdmin):
    list_display = ("nombre", "pais_origen", "debut")

@admin.register(Album)
class AlbumAdmin(admin.ModelAdmin):
    list_display = ("titulo", "grupo", "fecha_lanzamiento", "precio")
