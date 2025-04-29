
class No:
    def __init__(self, valor):
        self.valor = valor
        self.proximo = None

class ListaLigada:
    def __init__(self):
        self.cabeca = None

    def adicionar(self, valor, posicao):
        novoNo = No(valor)
        if self.cabeca is None or posicao == 0:
            novoNo.proximo = self.cabeca
            self.cabeca = novoNo
            return
        atual = self.cabeca
        i = 0
        while i < posicao - 1 and atual.proximo is not None:
            atual = atual.proximo
            i += 1
        novoNo.proximo = atual.proximo
        atual.proximo = novoNo
        
    def remover(self, valor):
        if self.cabeca is None:
            return
        if self.cabeca.valor == valor:
            self.cabeca = self.cabeca.proximo
            return
        atual = self.cabeca
        while atual.proximo is not None and atual.proximo.valor != valor:
            atual = atual.proximo
        if atual.proximo is not None:
            atual.proximo = atual.proximo.proximo

    def imprimir(self):
        atual = self.cabeca
        while atual is not None:
            print(atual.valor)
            atual = atual.proximo
        print("None")

