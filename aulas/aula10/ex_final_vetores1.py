# Considere o valor do vetor abaixo para fazer os próximos exercícios:
v1 = [41, 72, 39, 4, 35, 4]

# Fazer um procedimento chamado ‘exibe_lista(l)’ que exiba os elementos da lista passada por parâmetro.
# Faça uma função chamada ‘conta_elementos(l)’ que tenha o mesmo efeito do len().
# Faça uma função chamada ‘retorna_indice(elemento)’ com a melhoria de retornar -1 caso o elemento não seja encontrado.
# Faça uma função chamada ‘busca(l,elemento)’ que tenha o mesmo efeito do count().
# Fazer uma função chamada ‘conta_inteiro(l)’ que conte quantos elementos inteiros existem em uma lista.


def exibe_lista(v):
    som = 0
    for _ in v:
        som += 1
    for x in range(som):
        print(v[x])


def conta_elementos(v):
    som = 0
    for _ in v:
        som += 1
    return som


def retorna_indice(v, elem):
    som = 0
    index = 0
    for _ in v:
        som += 1
    for x in range(som):
        if elem == v[x]:
            index = x
            break
        else:
            index = -1
    return index


def busca(v, elem):
    tem = False
    v.sort()
    for x in range(len(v) - 1):
        if elem == v[x]:
            tem = True
            break
        else:
            tem = False
    if tem:
        som = 1
        for a in range(len(v) - 1):
            if elem == v[a] == v[a + 1]:
                som += 1
    else:
        som = 0
    return som


def conta_inteiro(v):
    som = 0
    for x in range(len(v)):
        if v[x] % 2 == 0 or v[x] % 2 == 1:
            som += 1
    return som


exibe_lista(v1)
print(conta_elementos(v1))
print(retorna_indice(v1, 72))
print(busca(v1, 72))
print(conta_inteiro(v1))
