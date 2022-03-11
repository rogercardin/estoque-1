import os

import django
from django.forms import DateField, DateTimeField

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "projeto.settings")
django.setup()

import string
import timeit
from random import choice, randint, random

from projeto.produto.models import Produto


class Utils:
    ''' Métodos genéricos. '''
    @staticmethod
    def gen_digits(max_length):
        return str(''.join(choice(string.digits) for i in range(max_length)))


class ProdutoClass:

    @staticmethod
    def criar_produtos(produtos):
        Produto.objects.all().delete()
        aux = []
        for produto in produtos:
            data = dict(
                equipamento=Utils.gen_digits(30),
                grandeza=Utils.gen_digits(30),
                chave_a=Utils.gen_digits(8),
                chave_b=Utils.gen_digits(8),
                chave_c=Utils.gen_digits(8),
                ultima_leitura=DateTimeField,
                leitura_anterior=DateField, 
                diferenca=float, max_digits=7, decimal_places=2,
                perc_diferenca=float, max_digits=7, decimal_places=2,
                situacao=float, max_digits=7, decimal_places=2,
            )
            obj = Produto(**data)
            aux.append(obj)
        Produto.objects.bulk_create(aux)


produtos = (
    'RE0997',
    'AMP',
    'A',
    'B',
    'C',
    '2022-01-06 13:13:00',
    '2022-01-06 13:00:00',
    '29.22',
    '7.34',
    '1.15',
    
)

tic = timeit.default_timer()

ProdutoClass.criar_produtos(produtos)


toc = timeit.default_timer()

print('Tempo:', toc - tic)
