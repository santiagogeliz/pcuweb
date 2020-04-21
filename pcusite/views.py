from django.shortcuts import render, get_object_or_404, redirect
from django.utils import timezone


def home_page(request):
	return render(request, 'pcusite/home_page.html', {})

def servicios(request):
	return render(request, 'pcusite/servicios.html', {})

def catalogo(request):
	return render(request, 'pcusite/catalogo.html', {})

def acero(request):
	return render(request, 'pcusite/acero.html', {})

def plastica(request):
	return render(request, 'pcusite/plastica.html', {})

def papelcarton(request):
	return render(request, 'pcusite/papelcarton.html', {})

def textil(request):
	return render(request, 'pcusite/textil.html', {})

def cemento(request):
	return render(request, 'pcusite/cemento.html', {})

def maderera(request):
	return render(request, 'pcusite/maderera.html', {})

def minera(request):
	return render(request, 'pcusite/minera.html', {})

def agricola(request):
	return render(request, 'pcusite/agricola.html', {})

def especiales(request):
	return render(request, 'pcusite/especiales.html', {})

def quienes_somos(request):
	return render(request, 'pcusite/quienes_somos.html', {})

def blog(request):
	return render(request, 'pcusite/blog.html', {})

def contacto(request):
	return render(request, 'pcusite/contacto.html', {})
