from django.db import models
from django.utils import timezone

class Post(models.Model):
	autor = models.ForeignKey('auth.User', on_delete=models.CASCADE)
	imagen = models.ImageField(max_length=100, upload_to='user_img/', null=True, blank=True)
	titulo = models.CharField(max_length=200)
	texto = models.TextField()
	fecha_creacion = models.DateTimeField(default=timezone.now)
	fecha_publicacion = models.DateTimeField(blank=True, null=True)

	def publicar(self):
		self.fecha_publicacion = timezone.now()
		self.save()

	def __str__(self):
		return self.title
