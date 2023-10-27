# Dado o valor de uma venda, exibir o orçamento.
# Sabendo-se que no crédito ascrecenta 1%.
# PIX e dinheiro, desconto de 5%.
# Débito é o valor da venda.

n1 = float(input("Valor da venda: "))
c = n1 * 1.01
v = n1 * 0.95
d = n1
print(f"Crédito: R${c:.2f}\n"
      f"PIX/Dinheiro: R${v:.2f}\n"
      f"Débito: R${d:.2f}")
