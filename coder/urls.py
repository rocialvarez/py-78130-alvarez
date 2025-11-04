# esto lo hago yo !! es personal

from django.urls import path
from coder.views import index, test, about, crear_cliente, crear_grupo, crear_album, albumes, lista_clientes, detalle_cliente, editar_cliente, eliminar_cliente, detalle_album


urlpatterns = [
    path("", index, name="index"),
    path("test/", test, name="test"),
    path("albumes/", albumes, name="albumes"),
    path("albumes/<int:pk>/", detalle_album, name="album_detail"),
    path("about/", about, name="about"),
    path("clientes/nuevo", crear_cliente, name="cliente_form"),
    path("grupos/nuevo", crear_grupo, name="grupo_form"),
    path("albums/nuevo", crear_album, name="album_form"),
    path("clientes/", lista_clientes, name="cliente_list"),
    path("clientes/<int:pk>/", detalle_cliente, name="cliente_detail"),
    path("clientes/<int:pk>/editar/", editar_cliente, name="cliente_edit"),
    path("clientes/<int:pk>/eliminar/", eliminar_cliente, name="cliente_delete"),

]