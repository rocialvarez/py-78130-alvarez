from django.shortcuts import render, get_object_or_404, redirect
from coder.forms import *
from coder.models import Cliente, Grupo, Album

# Create your views here. nota del profe: lógica de las apps, APIS

def index(request):
    return render(request, "coder/index.html")

def test(request):
    return render(request, "coder/test.html")

def albumes(request):
    albumes = Album.objects.all().order_by("titulo")
    return render(request, "coder/albumes.html", {"albumes": albumes})

def about(request):
    return render(request, "coder/about.html")

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

def detalle_cliente(request, pk):
    cliente = get_object_or_404(Cliente, pk=pk)
    return render(request, "coder/cliente_detail.html", {"cliente": cliente})

def editar_cliente(request, pk):
    cliente = get_object_or_404(Cliente, pk=pk)
    if request.method == "POST":
        form = ClienteForm(request.POST, instance=cliente)
        if form.is_valid():
            form.save()
            return redirect("cliente_list")
    else:
        form = ClienteForm(instance=cliente)
    return render(request, "coder/cliente_form.html", {"form":form})

def eliminar_cliente(request, pk):
    cliente = get_object_or_404(Cliente, pk=pk)
    if request.method == "POST":
        cliente.delete()
        return redirect("cliente_list")
    return render(request, "coder/cliente_confirm_delete.html", {"cliente": cliente})

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

def detalle_album(request, pk):
    album = get_object_or_404(Album, pk=pk)
    return render(request, "coder/album_detail.html", {"album": album})
