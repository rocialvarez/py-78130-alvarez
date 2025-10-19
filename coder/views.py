from django.shortcuts import render, redirect
from coder.forms import *
from coder.forms import Estudiante

# Create your views here. nota del profe: lógica de las apps, APIS

def index(request):
    return render(request, "coder/index.html")

def test(request):
    return render(request, "coder/test.html")

def albumes(request):
    return render(request, "coder/albumes.html")

def crear_estudiante(request):


    if request.method == "POST":
        form = EstudianteForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("estudiante_form")
    else:
        form = EstudianteForm()

    return render(request, "coder/estudiante_form.html", {'form': form})

def lista_estudiantes(request):
    query = request.GET.get('q', '')
    if len(query) > 0:
        estudiante = Estudiante.objects.filter(
            nombre__icontaines=query).order_by("-nro_legajo") 
    else:
        estudiante = Estudiante.objects.all().order_by("-nro_legajo")

    return render(request, "coder/estudiante_list.html", {"estudiantes": estudiante, "query": query})
