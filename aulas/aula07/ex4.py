# Criar uma função que pegue um numero e o multiplo por parâmetro e retorne o próximo numero multiplo
#       print(prox_mult(16, 7))  >> 21

def prox_mult(n1, n2):
    param = 1
    x = n1
    while param != 0:
        x += 1
        param = x % n2
    return x


print(prox_mult(16, 7))
