# Somar números até que o usuário digite um número negativo

n = 1
x = 0
while n >= 0:
    n = float(input("Digite número a somar: "))
    x += n
print(f"A somatória é: {x}")
