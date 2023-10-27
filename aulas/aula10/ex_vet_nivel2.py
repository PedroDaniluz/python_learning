# Considere o valor dos vetores abaixo para fazer os próximos exercícios:
v1 = [41, 72, 39, 4, 35]
v2 = [0, 0, 0, 0, 0]

# Fazer um procedimento chamado "copia_vetor", que copie os elementos do vetor 1 no vetor 2
# Fazer um procedimento chamado "inverte_vetor" que copie os elemenentos invertidos do v1 em v2
# Fazer um procedimento chamado "ordena_vetor_crescente" que ordene de forma crescente o vetor
# Fazer um procedimento chamado "ordena_vetor_decrescente" que ordene  de forma decrescente o vetor


def copia_vetor(va, vb):
    x = 0
    while x < len(va):
        y = va[x]
        vb[x] = y
        x += 1
    print(vb)


def inverte_vetor(va, vb):
    x = len(va) - 1
    y = 0
    while x >= 0:
        vb[x] = va[y]
        x -= 1
        y += 1
    print(vb)


def ordena_vetor_crescente(v):
    y = len(v) - 1
    a = 0
    while a < y:
        x = 0
        while x < y:
            if v[x] > v[x+1]:
                v[x], v[x+1] = v[x+1], v[x]
            x += 1
        a += 1
    print(v)


def ordena_vetor_decrescente(v):
    y = len(v) - 1
    a = 0
    while a < y:
        x = 0
        while x < y:
            if v[x] < v[x + 1]:
                v[x], v[x + 1] = v[x + 1], v[x]
            x += 1
        a += 1
    print(v)
