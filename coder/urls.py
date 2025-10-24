# esto lo hago yo !! es personal

from django.urls import path
from coder.views import index, test, crear_cliente, crear_grupo, crear_album, albumes, lista_clientes


urlpatterns = [
    path("", index, name="index"),
    path("test/", test, name="test"),
    path("albumes", albumes, name="albumes"),
    path("clientes/nuevo", crear_cliente, name="cliente_form"),
    path("grupos/nuevo", crear_grupo, name="grupo_form"),
    path("albums/nuevo", crear_album, name="album_form"),
    path("clientes/", lista_clientes, name="cliente_list"),
]