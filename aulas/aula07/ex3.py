# Criar uma função que pegue o numero passado por parâmetro e retorne o próximo numero multiplo de 5
#       print(prox_mult_5(7))

def prox_mult_5(n1):
    param = 1
    x = n1
    while param != 0:
        x += 1
        param = x % 5
    return x


print(prox_mult_5(91))
