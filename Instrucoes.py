from enum import Enum
from Contexto import Contexto


def proximaEtapa(contexto : Contexto):
    contexto.pc = contexto.pc.proximo

def ajustarValor(contexto : Contexto) -> str:
    valor = contexto.pc.valor
    if valor[0] != '#' and contexto.data[valor]:
        valor = str(contexto.data[valor])
        return valor.replace('#', '')

def add(contexto : Contexto):
    valor = ajustarValor(contexto)
    contexto.acc = int(contexto.acc) + int(valor)
    proximaEtapa(contexto)

def sub(contexto : Contexto):
    valor = ajustarValor(contexto)
    contexto.acc = int(contexto.acc) - int(valor)
    proximaEtapa(contexto)

def mult(contexto : Contexto):
    valor = ajustarValor(contexto)
    contexto.acc = int(contexto.acc) * int(valor)
    proximaEtapa(contexto)

def div(contexto : Contexto):
    valor = ajustarValor(contexto)
    contexto.acc = int(contexto.acc) // int(valor)
    proximaEtapa(contexto)

def load(contexto : Contexto): 
    contexto.acc = ajustarValor(contexto)
    proximaEtapa(contexto)

def store(contexto : Contexto):
    valor = contexto.pc.valor
    contexto.data[valor] = contexto.acc
    proximaEtapa(contexto)

def brany(contexto : Contexto):
    valor = contexto.pc.valor
    contexto.pc = contexto.flags[valor]

def brpos(contexto : Contexto):
    valor = contexto.pc.valor
    if int(contexto.acc) > 0:
            contexto.pc = contexto.flags[valor]
    else:
        proximaEtapa(contexto)

def brzero(contexto : Contexto):
        valor = contexto.pc.valor
        # print(f"chamou o brzero: {contexto}")
        if int(contexto.acc) == 0:
            contexto.pc = contexto.flags[valor]
        else:
            proximaEtapa(contexto)

def brneg(contexto : Contexto):
        valor = contexto.pc.valor
        if int(contexto.acc) < 0:
            contexto.pc = contexto.flags[valor]
        else:
            proximaEtapa(contexto)

def syscall(contexto : Contexto):
    valor = contexto.pc.valor
    if valor == "0":
        print("SYSCALL 0")
        return ReturnCode.EXIT
    elif valor == "1":
        print("SYSCALL 1")
        print(f"ACC = {contexto.acc}")
        proximaEtapa(contexto)
        return ReturnCode.OUTPUT
    elif valor == "2":
        print("SYSCALL 2")
        valid_value = False
        new_acc = 0
        while not valid_value:
            try:
                input_raw = input("Insira o novo valor para o acumulador (numero inteiro): ")
                new_acc = int(input_raw)
                valid_value = True
            except ValueError:
                print("Valor inserido invalido. Tente novamente.")
                valid_value = False

        contexto.acc = new_acc
        proximaEtapa(contexto)
        return ReturnCode.INPUT

class ReturnCode(Enum):
    EXIT = 0
    OUTPUT = 1
    INPUT = 2

instrucoes = {
    'ADD': add,
    'SUB': sub,
    'MULT': mult,
    'DIV': div,
    'LOAD': load,
    'STORE': store,
    'BRANY': brany,
    'BRPOS': brpos,
    'BRZERO': brzero,
    'BRNEG': brneg,
    'SYSCALL': syscall,
}