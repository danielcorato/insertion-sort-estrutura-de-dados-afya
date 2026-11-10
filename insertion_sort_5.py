import random
from time import perf_counter


def insertion_sort_teste(lista):
    comparacoes = 0
    movimentacoes = 0

    for i in range(1, len(lista)):
        atual = lista[i]
        j = i - 1

        while j >= 0:
            comparacoes += 1

            if lista[j] > atual:
                lista[j + 1] = lista[j]
                movimentacoes += 1
                j -= 1
            else:
                break

        lista[j + 1] = atual
        movimentacoes += 1

    return comparacoes, movimentacoes


tamanhos = [100, 1000, 5000]

for tamanho in tamanhos:
    dados_aleatorios = list(range(tamanho))
    random.shuffle(dados_aleatorios)

    dados_ordenados = list(range(tamanho))
    dados_inversos = list(range(tamanho - 1, -1, -1))

    testes = [
        ("Aleatoria", dados_aleatorios),
        ("Ordenada", dados_ordenados),
        ("Inversa", dados_inversos)
    ]

    for tipo, dados in testes:
        lista = dados.copy()

        inicio = perf_counter()
        comparacoes, movimentacoes = insertion_sort_teste(lista)
        fim = perf_counter()

        tempo = fim - inicio

        print(
            f"Tamanho: {tamanho} | "
            f"Entrada: {tipo} | "
            f"Tempo: {tempo:.6f} s | "
            f"Comparacoes: {comparacoes} | "
            f"Movimentacoes: {movimentacoes}"
        )
