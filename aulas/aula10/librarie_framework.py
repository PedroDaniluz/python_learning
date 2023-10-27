def primeiro_elemento(x):
    return x[0]


def exibe_negativo(x):
    print("Números negativos:", end=" ")
    for y in range(0, len(x), 1):
        if x[y] <= 0:
            print(x[y], end="; ")
        y += 1
    print()


def soma_elementos(x):
    soma = 0
    for y in range(0, len(x), 1):
        soma += x[y]
        y += 1
    return soma


def media_elementos(x):
    soma = 0
    for y in range(0, len(x), 1):
        soma += x[y]
        y += 1
    m = soma / len(x)
    return m


def elementos_impares(x):
    print("Números ímpares:", end=" ")
    for y in range(0, len(x), 1):
        if x[y] % 2 != 0:
            print(x[y], end="; ")
        y += 1
    print()