'''
Code by Rafael Henrique
https://bit.ly/2FLDHsH
'''

import csv
from vota_escola.models import Aluno

def csv_to_list(filename: str) -> list:
    with open(filename) as csv_file:
        reader = csv.DictReader(csv_file, delimiter=',')
        csv_data = [line for line in reader]
    return csv_data

def save_data(data):
    aux = []
    for item in data:
        try:
            obj = Aluno(
            nome_aluno=str(item.get('nome_aluno')),
            imagem=None,
            ra=str(item.get('ra')),
            rg=str(item.get('rg')),
            status=item.get('status'),
            nome_escola_id=item.get('nome_escola_id'),
            turma_atual_id=item.get('turma_atual_id')
            )
            aux.append(obj)
        except:
            print(f'Houve algum erro nos dados no item {item}')
    Aluno.objects.bulk_create(aux)

data = csv_to_list('carga.csv')
save_data(data)