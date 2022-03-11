import xlrd

from projeto.produto.models import Produto


def import_xlsx(filename):
    '''
    Importa planilhas xlsx.
    '''
    workbook = xlrd.open_workbook(filename)
    sheet = workbook.sheet_by_index(0)

    fields = ('equipamento', 'grandeza', 'chave_a','chave_b', 'chave_c', 'ultima_leitura','leitura_anterior', 'diferenca', 'perc_diferenca','situacao')

    
    aux = []
    for row in range(1, sheet.nrows):
        equipamento = sheet.row(row)[0].value
        grandeza = sheet.row(row)[1].value
        chave_a = sheet.row(row)[2].value
        chave_b = sheet.row(row)[3].value
        chave_c = sheet.row(row)[4].value
        ultima_leitura = sheet.row(row)[5].value
        leitura_anterior = sheet.row(row)[6].value
        diferenca = sheet.row(row)[7].value
        perc_diferenca = sheet.row(row)[8].value
        situacao = sheet.row(row)[9].value
       

        produto = dict(
            equipamento =equipamento,
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

       
    Produto.objects.all().delete()  # CUIDADO
    Produto.objects.bulk_create(aux)
