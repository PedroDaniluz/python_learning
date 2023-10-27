# Pedro Daniluz - RM97697

import os

tabela = list()


def preencher():
    registro = {
        'espécie': esp.upper(),
        'nome': nome.upper(),
        'raça': raca.upper(),
        'idade': idade,
        'dono': dono.upper()
    }
    tabela.append(registro.copy())


def exibir(indice: int):
    if len(tabela) > 0:
        print(f"Espécie.......: {tabela[indice]['espécie']}")
        print(f"Nome..........: {tabela[indice]['nome']}")
        print(f"Raça..........: {tabela[indice]['raça']}")
        print(f"Idade.........: {tabela[indice]['idade']} ANOS")
        print(f"Dono..........: {tabela[indice]['dono']}\n")
        input("Digite qualquer coisa para continuar: ")
    else:
        print("O registro está vazio!")


def exibir_tudo():
    if len(tabela) > 0:
        for i in range(0, len(tabela), 1):
            print(f"Nº do Animal........: {i}")
            print(f"Espécie.......: {tabela[i]['espécie']}")
            print(f"Nome..........: {tabela[i]['nome']}")
            print(f"Raça..........: {tabela[i]['raça']}")
            print(f"Idade.........: {tabela[i]['idade']} ANOS")
            print(f"Dono..........: {tabela[i]['dono']}\n")
        input("Digite qualquer coisa para continuar: ")
    else:
        print("O registro está vazio!")


while True:
    os.system('cls' if os.name == 'nt' else 'clear')
    print("MENU")
    print("0 - Sair")
    print("1 - Registrar animal")
    print("2 - Exibir animal específico")
    print("3 - Exibir todos os animais")
    opc = input("Escolha um opção: ")
    while not opc.isnumeric() or int(opc) < 0 or int(opc) > 3:
        opc = input("Digite um valor válido: ")

    match int(opc):
        case 0:
            break
        case 1:
            os.system('cls' if os.name == 'nt' else 'clear')
            esp = input("Digite a espécie do animal: ")
            nome = input("Digite o nome do animal: ")
            raca = input("Digite a raça do animal: ")
            idade = input("Digite a idade do animal em anos: ")
            while not idade.isnumeric() or int(idade) < 0:
                idade = input("Digite um valor válido: ")
            dono = input("Digite o nome do dono: ")
            preencher()
        case 2:
            os.system('cls' if os.name == 'nt' else 'clear')
            index = input("Digite o número do animal que deseja buscar: ")
            while not index.isnumeric() or int(index) < 0 or int(index) >= len(tabela):
                index = input("Digite um valor válido: ")
            exibir(int(index))
        case 3:
            os.system('cls' if os.name == 'nt' else 'clear')
            exibir_tudo()
