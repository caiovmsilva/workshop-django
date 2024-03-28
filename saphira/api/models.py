from django.db import models

class Usuario(models.Model):
    nomeCompleto = models.CharField(max_length=200)
    email = models.EmailField()
    cpf = models.CharField(max_length=14)

class Palestra(models.Model):
    titulo = models.CharField(max_length=200)
    descricao = models.TextField()

class Presenca(models.Model):
    usuario = models.ForeignKey(Usuario, on_delete=models.CASCADE)
    palestra = models.ForeignKey(Palestra, on_delete=models.CASCADE)
    presencial = models.BooleanField(default=False)
