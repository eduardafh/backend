from django.db import models

# Create your models here.
class Estado(models.Model):
    nome = models.CharField(max_length=50)
    sigla = models.CharField(max_length=2)
    
    def __str__(self):
        return f"{self.nome} ({self.sigla})"

class Cidade (models.Model):
    nome = models.CharField(max_length=50)
    estado = models.ForeignKey(Estado, on_delete=models.PROTECT)
    
    def __str__(self):
        return f"{self.nome} ({self.estado.sigla})"
    
class Pessoa (models.Model):
    nome = models.CharField(max_length=50)
    telefone = models.CharField(max_length=15)
    email = models.EmailField()
    data_nascimento = models.DateField()
    cidade = models.ForeignKey(Cidade, on_delete=models.PROTECT)

    def __str__(self):
        return f"{self.nome}"
    
