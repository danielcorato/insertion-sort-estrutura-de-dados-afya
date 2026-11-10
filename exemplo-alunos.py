def insertion_sort(alunos):
    comparacoes = 0
    movimentacoes = 0

#percorre os elementos a partir do segundo 
    for i in range(1, len(alunos)):
        #guarda o aluno que será inserido na posição correta 
        atual = alunos[i]
        j = i - 1
        
        #percorre os elementos anteriores 
        while j >= 0:
            comparacoes += 1
            
            #verifica se a nota anterior é maior que a atual 
            if alunos[j]["nota"] > atual["nota"]:
                #desloca pra direita o aluno com a nota maior 
                alunos[j + 1] = alunos[j]
                movimentacoes += 1
                j -= 1
            else:
                break
        
        #coloca o aluno na posição correta 
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