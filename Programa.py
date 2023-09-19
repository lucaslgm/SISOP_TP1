from dataclasses import dataclass
from Mnemonico import Mnemonico


@dataclass
class Programa:
    instrucao: 'Mnemonico' # Instruções a serem executadas pelo programa
    data: dict[str, int] # Armazenar variaveis e valores
    flags:[str, 'Mnemonico'] # Armaneza as flags e suas instruções

    def __init__(self):
        self.instrucao = None
        self.data = dict()
        self.flags = dict()
        
    def __str__(self) -> str:
        return f"Instrução = {self.instrucao}, data = {self.data}, flags = {self.flags}"