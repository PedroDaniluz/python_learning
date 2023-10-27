hu = 0
ze = 0
lu = 0

print("""
CANDIDATOS
1 - Huguinho
2 - Zezinho
3 - Luizinho
0 - Fim da Votação""")

while True:
    x = int(input("VOTO: "))
    match x:
        case 0:
            break
        case 1:
            hu += 1
        case 2:
            ze += 1
        case 3:
            lu += 1
        case _:
            print("Votação Inválida")

ac = hu + ze + lu

print(f"""
TOTAL DE VOTOS => {ac}
1 - HUGUINHO => {hu}
2 - ZEZINHO => {ze}
3 - LUIZINHO => {lu}""")
