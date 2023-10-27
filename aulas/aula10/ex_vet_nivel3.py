# Considere o valor dos vetores abaixo para fazer os próximos exercícios:
v1 = [41, 72, 39, 4, 35]
v2 = [0, 0, 0, 0, 0]

# Fazer um procedimento chamado "ordena_vetor" que ordene o vetor na forma solicitada (cresc. ou decresc.)
# Fazer um procedimento chamado "separa_pares_impares" que coloque os números pares antes dos ímpares
# Fazer uma função chamada "conta_acima_media" retorna a quntidade de elementos da lista estão acima da média
# Fazer uma função chamada "maior_elemento" que retorna o mair elemento da lista


def ordena_vetor(v):
    while True:
        form = input("Ordenar de forma [C]rescente ou [D]ecrescente?").upper()
        if form == "C" or form == "D":
            break
        else:
            print("OPÇÃO INVÁLIDA")
    if form == "C":
        y = len(v) - 1
        a = 0
        while a < y:
            x = 0
            while x < y:
                if v[x] > v[x + 1]:
                    v[x], v[x + 1] = v[x + 1], v[x]
                x += 1
            a += 1
    elif form == "D":
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


def separa_pares_impares(v):
    y = len(v) - 1
    a = 0
    while a < y:
        x = 0
        while x < y:
            if v[x] % 2 != 0 and v[x + 1] % 2 == 0:
                v[x], v[x + 1] = v[x + 1], v[x]
            x += 1
        a += 1
    print(v)


def conta_acima_media(v):
    y = len(v) - 1
    x = 0
    som = 0
    while x < y:
        som += v[x]
        x += 1
    med = som / len(v)
    x = 0
    cont = 0
    while x < y:
        if v[x] > med:
            cont += 1
        x += 1
    return cont


def maior_elemento(v):
    y = len(v) - 1
    a = 0
    while a < y:
        x = 0
        while x < y:
            if v[x] > v[x + 1]:
                v[x], v[x + 1] = v[x + 1], v[x]
            x += 1
        a += 1
    return v[-1]


ordena_vetor(v1)
separa_pares_impares(v1)
print(conta_acima_media(v1))
print(maior_elemento(v1))
