import os

tabela = list()
pessoa = dict()


def cadastrar(t: list, d: dict) -> None:
    os.system("clear")
    print("***** Cadastro Individual *****\n")
    d['nome'] = input("Nome: ")
    d['endereço'] = input("Endereço: ")
    t.append(d.copy())


def cadastro_mult(t: list, d: dict) -> None:
    while True:
        os.system("clear")
        print("***** Cadastro Múltiplo *****\n")
        x = input("Nome: ")
        if x == ".":
            break
        else:
            d['nome'] = x
            d['endereço'] = input("Endereço: ")
            t.append(d.copy())


def exibir(t: list) -> None:
    os.system("clear")
    print("***** Exibir Registro *****\n")
    if len(t) == 0:
        print("A tabela está vazia!")
    for i in range(0, len(t), 1):
        print(f"Pessoa.......{i}")
        print(f"Nome:........{t[i]['nome']}")
        print(f"Endereço:....{t[i]['endereço']}\n")
    input("Digite algo para prosseguir:")


def consultar(t: list) -> None:
    os.system("clear")
    print("***** Consultar Registro *****\n")
    busca = input("Digite nome da pessoa: ")
    x = 0
    for i in range(0, len(t), 1):
        if t[i]['nome'].upper() == busca.upper():
            x = 1
            os.system("clear")
            print(f"\"{busca.upper()}\" encontrado(a)")
            print(f"Endereço:.......{t[i]['endereço']}\n")
            input("Digite algo para continuar: ")
            break
    if x == 0:
        print(f"\"{busca.upper()}\" não encontrado(a)")
        input("Digite algo para continuar: ")


def alterar(t: list) -> None:
    os.system("clear")
    print("***** Alterar Registro *****\n")
    busca = input("Digite nome da pessoa: ")
    x = 0
    for i in range(0, len(t), 1):
        if t[i]['nome'].upper() == busca.upper():
            x = 1
            t[i]['endereço'] = input("Digite o novo Endereço: ")
            input("Cadastro atualizado. Digite algo para continuar: ")
            break
    if x == 0:
        print(f"\"{busca.upper()}\" não encontrado(a)")
        input("Digite algo para continuar: ")


def excluir(t: list) -> None:
    os.system("clear")
    print("***** Excluir Registro *****\n")
    busca = input("Digite nome da pessoa: ")
    x = 0
    for i in range(0, len(t), 1):
        if t[i]['nome'].upper() == busca.upper():
            x = 1
            t.pop(i)
            input("Cadastro removido. Digite algo para continuar: ")
            break
    if x == 0:
        print(f"\"{busca.upper()}\" não encontrado(a)")
        input("Digite algo para continuar: ")


while True:
    os.system("clear")
    print("""
    0 - SAIR
    1 - CADASTRAR
    2 - CADASTRO MÚLTIPLO
    3 - EXIBIR
    4 - CONSULTAR
    5 - ALTERAR
    6 - Excluir
    """)
    opc = input("Escolha: ")
    while not opc.isnumeric() or int(opc) > 6 or int(opc) < 0:
        opc = input("Escolha uma opção válida: ")
    match int(opc):
        case 0:
            break
        case 1:
            cadastrar(tabela, pessoa)
        case 2:
            cadastro_mult(tabela, pessoa)
        case 3:
            exibir(tabela)
        case 4:
            consultar(tabela)
        case 5:
            alterar(tabela)
        case 6:
            excluir(tabela)
