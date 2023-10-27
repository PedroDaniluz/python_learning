c1 = 0
c2 = 0
c3 = 0
n = 0
x1 = input("Digite o nome do primeiro candidato: ").upper()
x2 = input("Digite o nome do segundo candidato: ").upper()
x3 = input("Digite o nome do terceiro candidato: ").upper()

print(f"""
CANDIDATOS
1 - {x1}
2 - {x2}
3 - {x3}
0 - Fim da Votação""")

while True:
    x = int(input("VOTO: "))
    match x:
        case 0:
            break
        case 1:
            c1 += 1
        case 2:
            c2 += 1
        case 3:
            c3 += 1
        case _:
            n += 1
            print("Votação anulada")

ac = c1 + c2 + c3 + n

print(f"""
TOTAL DE VOTOS => {ac}
1 - {x1} => {c1} // {c1 / ac * 100:.2f}% dos votos
2 - {x2} => {c2} // {c2 / ac * 100:.2f}% dos votos
3 - {x3} => {c3} // {c3 / ac * 100:.2f}% dos votos
4 - NULOS => {n} // {n / ac * 100:.2f}% dos votos""")
