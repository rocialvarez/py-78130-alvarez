from django import forms
from coder.models import Estudiante, Grupo, Album

class EstudianteForm(forms.ModelForm):
    class Meta:
        model = Estudiante
        fields = ["nombre", "apellido", "email", "nro_legajo", "fecha_de_nacimiento"]
        widgets = {
            "fecha_de_nacimiento": forms.DateInput(attrs={'type': 'date', 'class': 'form-control'}),
            "nombre": forms.TextInput(attrs={'class': 'form-control'}),
            "apellido": forms.TextInput(attrs={'class': 'form-control'}),
            "email": forms.EmailInput(attrs={'class': 'form-control'}),
            "nro_legajo": forms.NumberInput(attrs={'class': 'form-control'})
        }

class GrupoForm(forms.ModelForm):
    class Meta:
        model = Grupo
        fields = ["nombre", "pais_origen", "debut"]
        widgets = {
            "nombre": forms.TextInput(attrs={'class': 'form-control'}),
            "pais_origen": forms.TextInput(attrs={'class': 'form-control'}),
            "debut": forms.DateInput(attrs={'type': 'date', 'class': 'form-control'}),
        }

class AlbumForm(forms.ModelForm):
    class Meta:
        model = Album
        fields = ["titulo", "grupo", "fecha_lanzamiento", "precio"]
        widgets = {
            "titulo": forms.TextInput(attrs={'class': 'form-control'}),
            "grupo": forms.Select(attrs={'class': 'form-select'}),
            "fecha_lanzamiento": forms.DateInput(attrs={'type': 'date', 'class': 'form-control'}),
            "precio": forms.NumberInput(attrs={'class': 'form-control'}),
        }