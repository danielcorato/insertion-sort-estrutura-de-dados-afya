def insertion_sort(alunos):
    comparacoes = 0
    movimentacoes = 0

    for i in range(1, len(alunos)):
        atual = alunos[i]
        j = i - 1

        while j >= 0:
            comparacoes += 1

            if alunos[j]["nota"] > atual["nota"]:
                alunos[j + 1] = alunos[j]
                movimentacoes += 1
                j -= 1
            else:
                break

        alunos[j + 1] = atual
        movimentacoes += 1

    return comparacoes, movimentacoes


# Aplicacao: notas dos alunos
alunos = []

quantidade = int(input("Quantos alunos deseja cadastrar? "))

for i in range(quantidade):
    nome = input("Digite o nome do aluno: ")
    nota = float(input("Digite a nota do aluno: "))

    aluno = {"nome": nome, "nota": nota}
    alunos.append(aluno)

print("\nAntes da ordenacao:")
for aluno in alunos:
    print(aluno["nome"], "-", aluno["nota"])

comparacoes, movimentacoes = insertion_sort(alunos)

print("\nDepois da ordenacao:")
for aluno in alunos:
    print(aluno["nome"], "-", aluno["nota"])

print("\nComparacoes:", comparacoes)
print("Movimentacoes:", movimentacoes)
