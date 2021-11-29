from django.db import models
from django.db.models.fields import EmailField

class Usuario(models.Model):
    nome = models.CharField(max_length=50)
    email = models.EmailField(max_length=45)
    senha = models.CharField(max_length=12)

class Administrador(models.Model):
    nome = models.CharField(max_length=50)
    email = models.EmailField(max_length=45)
    senha = models.CharField(max_length=12)
    