from django.shortcuts import render

# Create your views here. nota del profe: lógica de las apps, APIS

def index(request):
    return render(request, "coder/index.html")
