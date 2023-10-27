# Pedro Daniluz, RM97697
# João Lourenço de Camargo Sardinha, RM551842

def exibe_div(nm: str):
    split_name = nm.split(" ")
    name = split_name[0]
    surname = " ".join(split_name[1:])
    print(f"Nome: {name}\nSobrenome: {surname}")


def conta_palavras(nm: str):
    split_name = nm.split(" ")
    palavras = len(split_name)
    print(f"O nome {nome} tem {palavras} palavras")


print("-------------------------------------------------")
print("       Bem vindo ao software Checkpoint 1        ")
print("-------------------------------------------------")

nome = ""
while True:
    print("                     MENU                        ")
    print("1 -        Digite um nome completo               ")
    print("2 -     Exibe separado o Nome do Sobrenome       ")
    print("3 - Conta quantas palavras há no nome completo   ")
    print("0 -                  SAIR                        ")
    print("-------------------------------------------------")

    numEntrada = int(input("Insira o número que corresponde a função desejada: "))
    match numEntrada:
        case 1:
            while True:
                nome = input("Digite um nome completo: ")
                if len(nome.split(" ")) < 2:
                    print("Nome inválido")
                else:
                    break
        case 2:
            if len(nome.split(" ")) >= 2:
                exibe_div(nome)
            else:
                print("Nome em branco, digite algo")
        case 3:
            if len(nome.split(" ")) >= 2:
                conta_palavras(nome)
            else:
                print("Nome em branco, digite algo")
        case 0:
            break
        case _:
            print("Opção Inválida")
