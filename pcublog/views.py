from django.shortcuts import render, get_object_or_404, redirect
from django.utils import timezone


def home_page(request):
	return render(request, 'pcublog/home_page.html', {})

def servicios(request):
	return render(request, 'pcublog/servicios.html', {})

def catalogo(request):
	return render(request, 'pcublog/catalogo.html', {})

def acero(request):
	return render(request, 'pcublog/acero.html', {})

def plastica(request):
	return render(request, 'pcublog/plastica.html', {})

def papelcarton(request):
	return render(request, 'pcublog/papelcarton.html', {})

def textil(request):
	return render(request, 'pcublog/textil.html', {})

def cemento(request):
	return render(request, 'pcublog/cemento.html', {})

def maderera(request):
	return render(request, 'pcublog/maderera.html', {})

def minera(request):
	return render(request, 'pcublog/minera.html', {})

def agricola(request):
	return render(request, 'pcublog/agricola.html', {})

def especiales(request):
	return render(request, 'pcublog/especiales.html', {})

def quienes_somos(request):
	return render(request, 'pcublog/quienes_somos.html', {})

def blog(request):
	return render(request, 'pcublog/blog.html', {})

def contacto(request):
	return render(request, 'pcublog/contacto.html', {})
