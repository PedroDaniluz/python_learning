# Dadas duas notas, calcular a média e verificar se está aprovado ou não (media 6 ao menos).
# As notas devem ser válidas, caso contrario, exibir uma mensagem de erro e encerrar o programa.
# Entrada: 4  5   Saida: reprovado com media 4.5
# Entrada: 4  89  Saida: Erro, a segunda nota é invalida
# Entrada: -5     Saida: Erro, a primeira nota é invalida

nota1 = float(input("Digite uma nota: "))
nota2 = float(input("Digite outra nota: "))
m = (nota1 + nota2) / 2

if (nota1 <= 0 or nota1 >= 10) and (nota2 <= 0 or nota2 >= 10):
    print("As duas notas são inválidas")
elif nota1 <= 0 or nota1 >= 10:
    print(f"A primeira nota '{nota1}' é inválida")
elif nota2 <= 0 or nota2 >= 10:
    print(f"A segunda nota '{nota2}' é inválida")
elif m >= 6:
    print("O aluno foi aprovado")
else:
    print("O aluno foi reprovado")
