# Process Control Block

# Estrutura de dados usada para representar um processo dentro do sistema operacional
# Mantém todas as infos que o S.O precisa para poder controlar a execução do processo

from Estados import Estados
from Mnemonico import Mnemonico
from Programa import Programa

class BlocoControleProcessos:
    pId: int # Indentificador do processo
    acc: int # Acumulador
    pc: Mnemonico # Ponteiro da instrução em execução
    estado: Estados # Estado do processo
    programa: Programa # Sequência de instruções a serem executadas, variaveis e valores em memória

    def __init__(self, pId : int, programa : Programa):
        self.pId = pId
        self.acc = 0
        self.pc = programa.instrucao        
        self.programa = programa
        self.estado = None