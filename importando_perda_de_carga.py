import csv
from projeto.produto.models import Produto


def csv_to_list(filename: str) -> list:
    
    with open(filename) as csv_file:
        reader = csv.DictReader(csv_file, delimiter=',')
        csv_data = [line for line in reader]
    return csv_data


def save_data(data):
    '''
    Salva os dados no banco.
    '''
    aux = []
    for item in data:
        equipamento = str(item.get('equipamento'))
        grandeza = str(item.get('grandeza'))
        chave_a = str(item.get('chave_a'))
        chave_b = str(item.get('chave_b'))
        chave_c = str(item.get('chave_c'))
        ultima_leitura = str(item.get('ultima_leitura'))
        leitura_anterior =str(item.get('leitura_anterior'))
        diferenca = float(item.get('diferenca'))
        perc_diferenca = float(item.get('perc_diferenca'))
        situacao = float(item.get('situacao'))
        
        obj = Produto(
            equipamento=equipamento,
            grandeza=grandeza,
            chave_a=chave_a,
            chave_b=chave_b,
            chave_c=chave_c,
            ultima_leitura=ultima_leitura,
            leitura_anterior=leitura_anterior,
            diferenca=diferenca,
            perc_diferenca=perc_diferenca,
            situacao=situacao,
        )
        aux.append(obj)
    #Produto.objects.bulk_create(aux)
    Produto.objects.bulk_create(aux)


data = csv_to_list('fix/perda_carga.csv')
save_data(data)
