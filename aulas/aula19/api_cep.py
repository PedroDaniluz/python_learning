import os
import requests

while True:
    os.system('cls' if os.name == 'nt' else 'clear')
    print(" ╔════════════════ MENU ══════════════════╗")
    print(" ║ 1 - Consultar CEP                      ║")
    print(" ║ 0 - Sair                               ║")
    print(" ╚════════════════════════════════════════╝")
    opc = input("Escolha uma opção: ")

    while not opc.isnumeric() or not 0 <= int(opc) <= 1:
        opc = input("Opção inválida! Tente novamente: ")

    match int(opc):
        case 0:
            break
        case 1:
            zpc = input("Digite o CEP: ")

            while not zpc.isnumeric() or len(zpc) != 8:
                zpc = input("Valor inválido! Digite somente os números: ")

            url = f"https://viacep.com.br/ws/{zpc}/json/"
            request = requests.get(url=url)
            result = request.json()

            if len(result) == 1:
                os.system('cls' if os.name == 'nt' else 'clear')
                print("CEP não encontrado!")
                input('\nDigite algo para continuar: ')
            else:
                os.system('cls' if os.name == 'nt' else 'clear')
                print(f"CEP: {result['cep']}")
                if result['logradouro'] != '':
                    print(
                        f"Localidade: {result['logradouro']}, "
                        f"{result['bairro']}, {result['localidade']} - {result['uf']}")
                else:
                    print(f"Localidade: {result['localidade']} - {result['uf']}")
                print(f"DDD: {result['ddd']}")
                input('\nDigite algo para continuar: ')
