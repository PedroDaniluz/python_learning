print("""
    1 - Cadastro
    2 - Consulta
    3 - Alteração 
    4 - Exclusão
""")

#               MODO BURRO DE SE FAZER ESCOLHAS

#            item = int(input("Digite a opção: "))
#
#            if item == 1:
#                print("Executando o cadastro...")
#            elif item == 2:
#                print("Executando a consulta...")
#            elif item == 3:
#                print("Executando a alteração...")
#            elif item == 4:
#                print("Executando a exclusão...")
#            else:
#                print("DIGITA UM CARALHO DE UM NUMERO CERTO FDP!!!")


# MODO MELHOR DE SER FAZER ESCOLHAS (command: match case)

item = int(input("Digite a opção: "))

match item:
    case 1:
        print("Executando o cadastro...")
    case 2:
        print("Executando a consulta...")
    case 3:
        print("Executando a alteração...")
    case 4:
        print("Executando a exclusão...")
    case _:
        print("DIGITA UM CARALHO DE UM NUMERO CERTO FDP!!!")
