# Pedro Daniluz; RM97697
# Maria Eduarda de Carvalho Goda; RM552276

def cresc_f(a, b):
    dif = a - b
    y = 0
    if a < b:
        dif = -dif
        while y <= dif:
            print(f"{a + y}", end=" ")
            y += 1
    elif a > b:
        while y <= dif:
            print(f"{b + y}", end=" ")
            y += 1
    else:
        print(a)


def cresc_a(a, b):
    y = 0
    if a < b:
        dif = (b - 1) - a
        while y < dif:
            print(f"{(a + 1) + y}", end=" ")
            y += 1

    elif b < a:
        dif = (a - 1) - b
        while y < dif:
            print(f"{(b + 1) + y}", end=" ")
            y += 1

    else:
        print(a)


def decr(a, b):
    dif = a - b
    y = 0
    if a < b:
        dif = -dif
        while y <= dif:
            print(f"{b - y}", end=" ")
            y += 1
    elif a > b:
        while y <= dif:
            print(f"{a - y}", end=" ")
            y += 1
    else:
        print(a)


menu = 1254
while menu != 0:
    menu = int(input("""\n
    MENU
    1 - INTERVALO
    2 - INTERVALO ABERTO E FECHADO
    3 - INTERVALO CRESCENTE OU DECRESCENTE
    0 - SAIR

    ESCOLHA: """))

    if menu == 1:
        print("\nINTERVALO")
        a = int(input("Primeiro número: "))
        b = int(input("Segundo número: "))
        cresc_f(a, b)

    elif menu == 2:
        print("\nINTERVALO ABERTO OU FECHADO")
        a = int(input("Primeiro número: "))
        b = int(input("Segundo número: "))
        c = str(input("[A]berto ou [F]echado: ")).upper()
        if c == "A":
            cresc_a(a, b)
        elif c == "F":
            cresc_f(a, b)
        else:
            print("OPÇÃO INVÁLIDA")

    elif menu == 3:
        print("\nINTERVALO CRESCENTE OU DECRESCENTE")

        a = int(input("Primeiro número: "))
        b = int(input("Segundo número: "))

        if a > b:
            decr(a, b)
        elif a < b:
            cresc_f(a, b)
        else:
            print(a)

    elif menu > 3 or menu < 0:
        print("\n    OPÇÃO INVÁLIDA")
