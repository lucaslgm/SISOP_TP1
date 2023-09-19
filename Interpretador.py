
from Contexto import Contexto
from LeitorDeArquivos import LeitorDeArquivos as Arquivo
from Mnemonico import Mnemonico
from Programa import Programa
from Instrucoes import instrucoes


class Interpretador:
    def __init__(self, url: str):
        self.url = url
        self.programa = None

    def interpretar(self):
        self.programa = Programa()

        linhas = Arquivo.LerTxt(self.url)

        ultimaInstrucao = None
        flag = False

        totalLinhas = len(linhas) - 1
        
        for i in range(totalLinhas):
            linha = linhas[i]

            if linha == '.code':
                i += 1
                linha = linhas[i]

                # Processa as linhas até encontrar '.endcode', indicando o fim da seção de código.
                while linha != '.endcode':
                    if ':' in linha:
                        # Se a linha contém um rótulo, registra-o no dicionário de flags.
                        linha = linha.split(':')
                        self.programa.flags[linha[0]] = None
                        flag = linha[0]
                        mnemonico = None
                    else:
                        # Se for uma instrução normal, divide a linha para obter nome e valor da instrução.
                        nome = linha.split(' ')[0].upper()
                        valor = linha.split(' ')[1]
                        instrucao = instrucoes[nome]
                        mnemonico = Mnemonico(
                            nome = nome,
                            valor = valor,
                            instrucao = instrucao,
                            proximo = None
                        )

                    # Adiciona a instrução à estrutura de árvore de instruções.
                    if ultimaInstrucao is None:
                        self.programa.instrucao = mnemonico
                    else:
                        if mnemonico is not None:
                            ultimaInstrucao.proximo = mnemonico

                    # Se houver um rótulo, associa o rótulo à instrução atual.
                    if flag and mnemonico is not None:
                        self.programa.flags[flag] = mnemonico
                        flag = False

                    # Atualiza a "última" instrução para a instrução atual.
                    if not flag:
                        ultimaInstrucao = mnemonico

                    i += 1
                    linha = linhas[i]

            i += 1
            linha = linhas[i]
            
            # Verifica se a linha contém '.data', indicando o início da seção de dados.
            if linha == '.data':
                i += 1
                linha = linhas[i]

                # Processa as linhas até encontrar '.enddata', indicando o fim da seção de dados.
                while linha != '.enddata':
                    variavel = linha.split(' ')[0]
                    valor = linha.split(' ')[1]

                    # Armazena a variável e seu valor no dicionário de dados do programa.
                    self.programa.data[variavel] = valor

                    i += 1
                    linha = linhas[i]

        # Retorna a instância da classe Program com as informações analisadas.
        return self.programa

    def interpretar2(self):
        self.programa = Programa()

        listaInstrucoes = Arquivo.LerTxt(self.url)
        linhas = iter(listaInstrucoes)

        ultimaInstrucao = None
        flag = False

        for linha in linhas:
            if linha == '.code':
                linha = next(linhas)
                # Processa as linhas até encontrar '.endcode', indicando o fim da seção de código.
                while linha != '.endcode':
                    if ':' in linha:
                        # Se a linha contém um rótulo, registra-o no dicionário de flags.
                        linha = linha.split(':')
                        self.programa.flags[linha[0]] = None
                        flag = linha[0]
                        mnemonico = None
                    else:
                        # Se for uma instrução normal, divide a linha para obter nome e valor da instrução.
                        nome = linha.split(' ')[0].upper()
                        valor = linha.split(' ')[1]
                        instrucao = instrucoes[nome]
                        mnemonico = Mnemonico(
                            nome = nome,
                            valor = valor,
                            instrucao = instrucao,
                            proximo = None
                        )

                    # Adiciona a instrução à estrutura de árvore de instruções.
                    if ultimaInstrucao is None:
                        self.programa.instrucao = mnemonico
                    else:
                        if mnemonico is not None:
                            ultimaInstrucao.proximo = mnemonico

                    # Se houver um rótulo, associa o rótulo à instrução atual.
                    if flag and mnemonico is not None:
                        self.programa.flags[flag] = mnemonico
                        flag = False

                    # Atualiza a "última" instrução para a instrução atual.
                    if not flag:
                        ultimaInstrucao = mnemonico

                    linha = next(linhas)

            # Verifica se a linha contém '.data', indicando o início da seção de dados.
            if linha == '.data':
                linha = next(linhas)

                # Processa as linhas até encontrar '.enddata', indicando o fim da seção de dados.
                while linha != '.enddata':
                    variavel = linha.split(' ')[0]
                    valor = linha.split(' ')[1]

                    # Armazena a variável e seu valor no dicionário de dados do programa.
                    self.programa.data[variavel] = valor

                    linha = next(linhas)
                    
        # Retorna a instância da classe Program com as informações analisadas.
        return self.programa