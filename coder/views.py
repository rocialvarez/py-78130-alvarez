from django.shortcuts import render, redirect
from coder.forms import *
from coder.models import Cliente, Grupo, Album

# Create your views here. nota del profe: lógica de las apps, APIS

def index(request):
    return render(request, "coder/index.html")

def test(request):
    return render(request, "coder/test.html")

def albumes(request):
    return render(request, "coder/albumes.html")

def crear_cliente(request):
    if request.method == "POST":
        form = ClienteForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("cliente_list")
    else:
        form = ClienteForm()
    return render(request, "coder/cliente_form.html", {'form': form})

def lista_clientes(request):
    query = request.GET.get('q', '')
    if query:
        clientes = Cliente.objects.filter(nombre__icontains=query).order_by("-id")
    else:
        clientes = Cliente.objects.all().order_by("-id")
    return render(request, "coder/cliente_list.html", {"clientes": clientes, "query": query})

def crear_grupo(request):
    if request.method == "POST":
        form = GrupoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("grupo_form")
    else:
        form = GrupoForm()
    return render(request, "coder/grupo_form.html", {'form': form})

def crear_album(request):
    if request.method == "POST":
        form = AlbumForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("album_form")
    else:
        form = AlbumForm()
    return render(request, "coder/album_form.html", {'form': form})