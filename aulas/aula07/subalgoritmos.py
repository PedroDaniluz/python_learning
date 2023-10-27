def saudacao(nome):
    print(f"Bom dia {nome}")


def saudacao2(nome, hora):
    if hora <= 12:
        msg = "Bom dia"
    elif 12 <= hora <= 18:
        msg = "Boa tarde"
    else:
        msg = "Boa noite"
    print(f"{msg}, {nome}!")


saudacao2("Pedro", 15)

#===========================================================

def raiz_2(n):
    return n ** (1/2)


print(raiz_2(121))

#===========================================================

def mA():
    ac = 0
    z = 0
    while True:
        x = float(input("(0 PARA SAIR) Digite valores para calcular a média: "))
        ac += x
        z += 1
    print(ac / z)


mA()
