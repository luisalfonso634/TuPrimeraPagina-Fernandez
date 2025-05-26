from django import forms
from .models import Autor, Post, Categoria

class AutorForm(forms.ModelForm):
    class Meta:
        model = Autor
        fields = ['nombre', 'email']

class CategoriaForm(forms.ModelForm):
    class Meta:
        model = Categoria
        fields = ['nombre']

class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['titulo', 'contenido', 'autor', 'categoria']

class BusquedaForm(forms.Form):
    termino_busqueda = forms.CharField(max_length=200, label="Término de búsqueda")