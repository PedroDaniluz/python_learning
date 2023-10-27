# Em uma votação, existem 3 candidatos: 1 – Huguinho, 2 – Zezinho e 3 –
# Luizinho. Pedir e acumular votos até a condição de saída
# que será "N". Ao final, exibir a quantidade de votos de cada usuário.

y = "S"
h = 0
z = 0
lu = 0

print("""1 - Huguinho
2 - Zezinho
3 - Luizinho""")

while y != "N":
    x = int(input("\nVote digitando o número correspondente ao canditato escolhido: "))
    match x:
        case 1:
            h += 1
        case 2:
            z += 1
        case 3:
            lu += 1
        case _:
            print("OPÇÃO INVÁLIDA")

    y = input("""
       Continuar votação?
       [s]im ou [n]ão: """).upper()

    if y != "S" and y != "N":
        print("Digite apenas [s] para sim ou [n] para não")
        continue

print(f"""HUGUINHO = {h} voto(s)
ZEZINHO = {z} voto(s)
LUIZINHO = {lu} voto(s)
""")
