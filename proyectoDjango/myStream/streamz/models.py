from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class user(models.Model):
    email = models.EmailField()
    username = models.CharField(max_length=50)
    password = models.CharField(max_length=16)


class Video(models.Model):
    usuario = models.CharField(max_length=50)
    imagen = models.ImageField(upload_to='videos/')    
    fecha_publicacion = models.DateTimeField(auto_now_add=True)    

class comentarios(models.Model):
    username = models.CharField(max_length=50)
    comentario = models.CharField(max_length=280)
    id_video = models.ForeignKey(Video,on_delete=models.CASCADE,null=True)