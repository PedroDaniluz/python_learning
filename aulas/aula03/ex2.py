# Uma maquininha de cartão cobra 2.39% caso a venda seja a crédito
# e 1.51% caso a venda seja a débito
# Fazer um programa que peça a venda, a forma de pagamento
# e exiba no final o valor da venda, o acrescimo e a venda acrescida

v = float(input("Qual é o valor da venda: R$"))
m = str(input("""
[C]rédito
[D]ébito
Digite o meio de pagamento: 
""")).upper()
c = v * 1.0239
d = v * 1.0151
b = v
ac = 0

if m == "C":
    ac = c - v
    b = c

elif m == "D":
    ac = d - v
    b = d

else:
    print("Opção inválida")

print(f"""
O valor inicial da venda é: R${v:8.2f}
O acréscimo é: R${ac:8.2f}
O Valor final será: R${b:8.2f}
""")
