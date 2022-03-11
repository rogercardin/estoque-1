from datetime import datetime
from django.db import models
from django.urls import reverse_lazy

class Produto(models.Model):
    equipamento = models.CharField(max_length=30)
    grandeza = models.CharField(max_length=30)
    chave_a = models.CharField(max_length=30, unique=True)
    chave_b = models.CharField(max_length=30)
    chave_c = models.CharField(max_length=30)
    ultima_leitura = models.CharField(max_length=30)
    leitura_anterior = models.CharField(max_length=30)
    diferenca = models.DecimalField('diferenca', max_digits=7, decimal_places=2)
    perc_diferenca = models.DecimalField('perc_diferenca', max_digits=7, decimal_places=2)
    situacao = models.DecimalField('situacao', max_digits=7, decimal_places=2)
    
    
    def get_absolute_url(self):
        return reverse_lazy('produto:produto_detail', kwargs={'pk': self.pk})

    def to_dict_json(self):
        return {
            'pk': self.pk,
            'produto': self.produto,
            'estoque': self.estoque,
        }



