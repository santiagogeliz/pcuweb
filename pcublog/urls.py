from django.urls import re_path, path
from . import views

urlpatterns = [
	re_path(r'^$', views.home_page, name = 'home_page'),
	re_path(r'^servicios$', views.servicios, name = 'servicios'),
	re_path(r'^catalogo$', views.catalogo, name = 'catalogo'),
	re_path(r'^catalogo/acero$', views.acero, name = 'acero'),
	re_path(r'^catalogo/plástica$', views.plastica, name = 'plastica'),
	re_path(r'^catalogo/papelcartón$', views.papelcarton, name = 'papelcarton'),
	re_path(r'^catalogo/textil$', views.textil, name = 'textil'),
	re_path(r'^catalogo/cemento$', views.cemento, name = 'cemento'),
	re_path(r'^catalogo/maderera$', views.maderera, name = 'maderera'),
	re_path(r'^catalogo/minera$', views.minera, name = 'minera'),
	re_path(r'^catalogo/agrícola$', views.agricola, name = 'agricola'),
	re_path(r'^catalogo/especiales$', views.especiales, name = 'especiales'),
	re_path(r'^quienes_somos$', views.quienes_somos, name = 'quienes_somos'),
	re_path(r'^blog$', views.blog, name = 'blog'),
	re_path(r'^contacto$', views.contacto, name = 'contacto'),

]