from dataclasses import dataclass


@dataclass
class LeitorDeArquivos:

    @staticmethod
    def LerTxt(url):
        arquivo = open(url, 'r')
        linhas = arquivo.readlines()
        arquivo.close()
        
        instrucoes = []

        for linha in linhas:
            instrucoes.append(linha.strip())

        return instrucoes