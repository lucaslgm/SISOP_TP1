# O deadline é igual ao período
# A prioridade é igual ao deadline - no EDF  quanto menor o dealine maior a prioridade

from BlocoControleProcessos import BlocoControleProcessos as PCB
from Interpretador import Interpretador
from Programa import Programa

class Processo:
    tempo_execucao: int
    deadline: int
    pcb : PCB

    def __init__(self, pId, deadline, tempo_execucao, url):
        programa: Programa = Interpretador(url).interpretar2()
        
        self.deadline = deadline
        self.tempo_execucao = tempo_execucao
        self.pcb = PCB(pId,programa)


    def __lt__(self, other):
        return self.deadline < other.deadline

    def __str__(self):
        instrucoes: str = ''
        instrucao = self.pcb.programa.instrucao
        while instrucao != None:
            aux: str = f'{instrucao.nome} {instrucao.valor}\n'
            instrucoes += aux
            instrucao = instrucao.proximo or None 
            
        return f"Processo(deadline={self.deadline}, Instruções:\n({instrucoes}))"