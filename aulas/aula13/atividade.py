# Pedro Daniluz, RM97697

from funcoes import *

while True:
    opc = int(input("""
    MENU:
    0 - SAIR
    1 - Converter Vogais
    2 - Verifica se é float
    
    Opção: """))

    if opc == 0:
        break
    elif opc == 1:
        x = input("Digite um texto: ")
        print(converte_vogais_maiusculo(x))
    elif opc == 2:
        x = input("Digite um número: ")
        if isfloat(x):
            print(f"O número '{x}' é float")
        else:
            print(f"O número '{x}' não é float")
    else:
        print("\nDigite um valor válido")
