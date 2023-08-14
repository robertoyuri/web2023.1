from django.db import models

# Create your models here.
class Cliente(models.Model):
    nome = models.CharField(max_length=20)
    cpf = models.CharField(max_length=11)
    idade = models.IntegerField()
    endereco = models.CharField(max_length=50)
    genero = models.CharField(max_length=1)
    def __str__(self):
        return self.cpf