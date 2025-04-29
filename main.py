from classes import ListaLigada

lista = ListaLigada()

with open("arq.txt", "r", encoding="utf-8-sig") as arquivo:
    linhas = arquivo.readlines()
valores = list(map(int, linhas[0].strip().split()))

for valor in reversed(valores):
    lista.adicionar(valor, 0)

for linha in linhas[1:]:
    partes = linha.strip().split()

    if len(partes) == 0:
        continue

    comando = partes[0]
    if comando == "A":
        valor = int(partes[1])
        posicao = int(partes[2])
        lista.adicionar(valor, posicao)

    elif comando == "R":

        valor = int(partes[1])
        lista.remover(valor)

    elif comando == "P":
        lista.imprimir() 