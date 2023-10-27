# Dado um número pelo usuário, apresente seu módulo matemático

n = float(input("Digite um número qualquer: "))
if n < 0:
    n = n * -1
print(f"O módulo desse número é: {n}")