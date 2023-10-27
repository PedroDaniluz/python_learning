# Dado um número, exibir os seus 10 primeiros múltiplos
x = int(input("Digite o número:"))
y = 1

while y <= 10:
    print(f"{x} * {y} = {x * y}")
    y += 1
