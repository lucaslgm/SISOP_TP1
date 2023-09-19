from dataclasses import dataclass


@dataclass
class Mnemonico:
    nome: str # Nome da instrução
    valor: str # Parametro da instrução
    instrucao: callable # Operação a ser executada
    proximo: 'Mnemonico' # Referencia a operação seguinte

    def __str__(self) -> str:
        return f'{self.nome} {self.valor}'