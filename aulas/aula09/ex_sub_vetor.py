# Fazer uma função que retorne o primeiro elemento do vetor (sub1)
# Fazer um procedimento que exiba somente os números negativos contidos no vetor (sub2)
# Fazer uma função que retorne a soma dos elementos do vetor (sub3)
# Fazer uma função que retorne a media dos elementos do vetor (sub4)
# Fazer um procedimento que exiba na tela os números ímpares contidos no vetor (sub5)

v = [45, -89, 32, -12, 33]


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


print(f"Primeiro número: {primeiro_elemento(v)}")
exibe_negativo(v)
elementos_impares(v)
print(f"Soma dos elementos: {soma_elementos(v)}")
print(f"Média dos elementos: {media_elementos(v)}")
