from django.shortcuts import render, get_object_or_404, redirect
from django.utils import timezone


def home_page(request):
	return render(request, 'groway/home_page.html', {})

def quienes_somos(request):
	return render(request, 'groway/quienes_somos.html', {})

def servicios(request):
	return render(request, 'groway/servicios.html', {})

def contacto(request):
	return render(request, 'groway/contacto.html', {})
