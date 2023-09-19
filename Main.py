from Interpretador import Interpretador
from Processo import Processo


# programa = Interpretador('Exemplos/prog1.txt').interpretar2()

# instrucao = programa.instrucao
# data = programa.data

# while instrucao != None:
#     print(f'{instrucao.nome} {instrucao.valor}')
#     instrucao = instrucao.proximo or None

# print(data)

url: str = 'Exemplos/prog1.txt'
processo = Processo(1,2,5, url)

print(processo)