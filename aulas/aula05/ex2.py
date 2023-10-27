# Somar números até que o usuário digite um número negativo,
# que não fará parte da somatória

n = 1
x = 0
while True:
    n = float(input("Digite um número: "))
    if n < 0:
        break
    x = x + n
print(f"A somatória é: {x}")
