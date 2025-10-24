from django.contrib import admin
from coder.models import *


@admin.register(Cliente)
class ClienteAdmin(admin.ModelAdmin):
    list_display = ("nombre", "apellido", "email", "fecha_de_nacimiento")
    list_display_links = ("nombre", "apellido")
    search_fields = ("nombre", "apellido", "email")
    list_filter = ("fecha_de_nacimiento",)
    ordering = ("apellido", "nombre")