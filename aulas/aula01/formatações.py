nome = "Pedro"
idade = 18
salario = 15870.25

# Forma 1 - Raiz
print(nome, idade, salario)
# Forma 2 - Raiz
print("nome:", nome, "idade:", idade, "salario:", salario)
# Forma 3 - Raiz o \n muda de linha ("dentro das aspas")
print("nome:", nome, "\nidade:", idade, "\nsalario:", salario)
# Forma 4 - O print exibe algo e muda de linha automaticamente
print("nome:", nome)
print("idade:", idade)
print("salario:", salario)

# Forma 5 - format()
print("Nome: {} \nIdade: {} \nSalário {}".format(nome, idade, salario))
# Forma 6 - format()                                                 0     1       2
print("Nome: {0} \nIdade: {1} \nSalário {2} \nObrigado {0}".format(nome, idade, salario))
# Forma 7 aliance
print("Nome: {n} \nIdade: {i} \nSalário {s}".format(n=nome, i=idade, s=salario))

# Forma 8 - print f
print(f"Nome: {nome} \nIdade: {idade} \nSalário {salario}")

# Forma 9 - print f
print(f"Nome: {nome} \nIdade: {idade:5d} \nSalário {salario:10.1f}")
v1 = 123.4
v2 = 4342.9595
v3 = 1.555
print(f"Valor 1 .....: R${v1:8.2f}")
print(f"Valor 1 .....: R${v2:8.2f}")
print(f"Valor 1 .....: R${v3:8.2f}")

# Forma 10
print("""
 caramba
 muita
 emoção
""")

print(f"""
    Valor 1.....: R${v1:8.2f}
    Valor 2.....: R${v2:8.2f}
    Valor 3.....: R${v3:8.2f}
""")
m = " "*4
print(m + "Segue acima os valores solicitados")