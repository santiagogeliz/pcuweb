from django.urls import re_path, path
from . import views

urlpatterns = [
	re_path(r'^$', views.home_page, name = 'home_page'),
	re_path(r'^quienes_somos$', views.quienes_somos, name = 'quienes_somos'),
	re_path(r'^servicios$', views.servicios, name = 'servicios'),
	re_path(r'^contacto$', views.contacto, name = 'contacto'),

]