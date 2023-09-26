from django.db import models

# Create your models here.
class Contato(models.Model):
    nome = models.CharField(max_length=150)
    email = models.EmailField()
    mensagem = models.CharField(max_length=3000)
    data = models.DateField(auto_now_add=True)
    
class Reserva(models.Model):
    nome_pet = models.CharField(max_length=50)
    telefone = models.CharField(max_length=15)    
    data_reserva = models.DateField()
    observacoes = models.CharField(max_length=3000)