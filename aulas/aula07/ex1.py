# Criar um procedimento que passe dois valores referentes a um intervalo e exiba os numeros do intervalo.

def interv(n1, n2):
    x = 0

    if n1 < n2:
        dif = n2 - n1
        while x <= dif:
            print(n1 + x)
            x += 1

    if n2 < n1:
        dif = n1 - n2
        while x <= dif:
            print(n2 + x)
            x += 1


interv(27, 20)
