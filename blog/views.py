from django.shortcuts import render, redirect
from .forms import AutorForm, CategoriaForm, PostForm, BusquedaForm
from .models import Autor, Post

def crear_autor(request):
    if request.method == 'POST':
        form = AutorForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('lista_autores')  # Redirige a la lista de autores
    else:
        form = AutorForm()
    return render(request, 'blog/crear_autor.html', {'form': form})

def crear_categoria(request):
    if request.method == 'POST':
        form = CategoriaForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('lista_categorias')  # Redirige a la lista de categorías
    else:
        form = CategoriaForm()
    return render(request, 'blog/crear_categoria.html', {'form': form})

def crear_post(request):
    if request.method == 'POST':
        form = PostForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('lista_posts')  # Redirige a la lista de posts
    else:
        form = PostForm()
    return render(request, 'blog/crear_post.html', {'form': form})

def buscar(request):
    query = request.GET.get('q', '')
    resultados = Post.objects.filter(titulo__icontains=query)
    return render(request, 'blog/resultados_busqueda.html', {'resultados': resultados, 'query': query})