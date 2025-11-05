from django.shortcuts import render, redirect
from django.contrib.auth import login, logout
from django.contrib.auth.decorators import login_required
from accounts.forms import *
from django.contrib import messages

# Create your views here.

def register(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            messages.success(request, f"¡Muy bien, {user.username}! Tu cuenta fue creada con exito.")
            return redirect('index') 
        else:
            messages.error(request, "Hubo un error en el formulario.")
    else:
        form = UserRegisterForm()

    return render(request, "accounts/registro.html", {"form": form})


@login_required
def perfil(request):
    return render(request, 'accounts/perfil.html')


@login_required
def perfil_edit(request):
    profile = request.user.profile
    if request.method == 'POST':
        form = ProfileForm(request.POST, request.FILES, instance=profile)
        if form.is_valid():
            form.save()
            messages.success(request, "Perfil actualizado con exito.")
            return redirect('profile')
    else:
        form = ProfileForm(instance=profile)
    return render(request, 'accounts/perfil_edit.html', {'form': form})


def salir(request):
    logout(request) 
    return redirect('index')