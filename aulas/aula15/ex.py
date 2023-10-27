# Crie um menu:
#    0 - Sair
#    1 - Preencher Registro
#    2 - Exibir Reistro

import os


def preencher(d: dict):
    key = input("Qual campo deseja preencher? (ex: nome, telefone...)")
    value = input("Qual valor deseja associar ao compo? ")
    d[key] = value


def exibe_dicionario(c: dict):
    for chave in c:
        tamanho = len(chave)
        tamanho = 20 - tamanho
        pontos = "." * tamanho
        print("\nCONTATO:")
        print(f"{chave}{pontos}: {c[chave]}")


contato = {}
while True:
    os.system("cls")
    opc = input("""             MENU
    0 - Sair
    1 - Preencher Contato
    2 - Exibir Contato
    
    Escolha uma opção: """)
    while not opc.isnumeric():
        opc = input("Digite um valor válido")
    match int(opc):
        case 0:
            break
        case 1:
            preencher(contato)
        case 2:
            exibe_dicionario(contato)
