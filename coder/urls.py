# esto lo hago yo !! es personal

from django.urls import path
from coder.views import index, test, crear_estudiante, crear_grupo, crear_album, albumes, lista_estudiantes


urlpatterns = [
    path("", index, name="index"),
    path("test/", test, name="test"),
    path("albumes", albumes, name="albumes"),
    path("estudiantes/nuevo", crear_estudiante, name="estudiante_form"),
    path("grupos/nuevo", crear_grupo, name="grupo_form"),
    path("albums/nuevo", crear_album, name="album_form"),
    path("estudiantes/", lista_estudiantes, name="estudiante_list"),
]