from django.shortcuts import render, redirect
from .forms import AutorForm, CategoriaForm, PostForm, BusquedaForm
from .models import Autor, Post

def crear_autor(request):
    if request.method == 'POST':
        form = AutorForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('lista_autores')  # Redirect to the list of authors
    else:
        form = AutorForm()
    return render(request, 'crear_autor.html', {'form': form})

def crear_categoria(request):
    if request.method == 'POST':
        form = CategoriaForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('lista_categorias')  # Redirect to the list of categories
    else:
        form = CategoriaForm()
    return render(request, 'crear_categoria.html', {'form': form})

def crear_post(request):
    if request.method == 'POST':
        form = PostForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('lista_posts')  # Redirect to the list of posts
    else:
        form = PostForm()
    return render(request, 'crear_post.html', {'form': form})

def buscar(request):
    query = request.GET.get('q', '')
    resultados = Post.objects.filter(titulo__icontains=query)
    return render(request, 'resultados_busqueda.html', {'resultados': resultados, 'query': query})

def index(request):
    return render(request, 'base.html')