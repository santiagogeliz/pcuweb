from django.shortcuts import render, get_object_or_404, redirect
from django.utils import timezone


def home_page(request):
	return render(request, 'pcublog/home_page.html', {})

def quienes_somos(request):
	return render(request, 'pcublog/quienes_somos.html', {})

def servicios(request):
	return render(request, 'pcublog/servicios.html', {})

def contacto(request):
	return render(request, 'pcublog/contacto.html', {})
