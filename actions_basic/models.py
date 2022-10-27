from django.db import models

class Produto(models.Model):
    nome = models.CharField(max_length=50)
    preco = models.DecimalField(max_digits=6, decimal_places=2)
    descricao = models.TextField()
    data_validade = models.DateTimeField()

    def __str__(self):
        return self.nome