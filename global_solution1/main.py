from librarie import *

while True:
    print("╔════════════════ MENU ══════════════════╗")
    print("║ 1 - Cadastrar alimento                 ║")
    print("║ 2 - Atualizar alimento                 ║")
    print("║ 3 - Remover alimento                   ║")
    print("║ 4 - Listar alimentos                   ║")
    print("║ 5 - Distribuir alimento                ║")
    print("║ 6 - Relatório de vencimentos           ║")
    print("║ 7 - Consultar alimento                 ║")
    print("║ 0 - Sair                               ║")
    print("╚════════════════════════════════════════╝")

    opcao = input("Digite a opção desejada: ")

    if opcao == "1":
        nome = input("Digite o nome do alimento: ").upper()
        print("Categoria do alimento:")
        print("1 - Fruta")
        print("2 - Verdura")
        print("3 - Legume")
        print("4 - Grão")
        print("5 - Outro")
        categoria_opcao = input("Digite o número correspondente à categoria ou 'Outro' para digitar: ")

        if categoria_opcao == "1":
            categoria = "Fruta"
        elif categoria_opcao == "2":
            categoria = "Verdura"
        elif categoria_opcao == "3":
            categoria = "Legume"
        elif categoria_opcao == "4":
            categoria = "Grão"
        else:
            categoria = input("Digite a categoria do alimento: ")

        data_validade_str = input("Digite a data de validade do alimento (no formato DD/MM/AAAA): ")
        quantidade = int(input("Digite a quantidade disponível do alimento: "))

        data_validade = datetime.datetime.strptime(data_validade_str, "%d/%m/%Y").date()
        cadastrar_alimento(nome, categoria, data_validade, quantidade)
        print("Alimento cadastrado com sucesso!")
        print()

    elif opcao == "2":
        nome = input("Digite o nome do alimento que deseja atualizar: ").upper()
        quantidade = int(input("Digite a nova quantidade disponível do alimento: "))
        atualizar_alimento(nome, quantidade)
        print("Alimento atualizado com sucesso!")
        print()

    elif opcao == "3":
        nome = input("Digite o nome do alimento que deseja remover: ").upper()
        remover_alimento(nome)
        print("Alimento removido com sucesso!")
        print()

    elif opcao == "4":
        listar_alimentos()
        print()

    elif opcao == "5":
        nome = input("Digite o nome do alimento que deseja distribuir: ").upper()
        quantidade = int(input("Digite a quantidade a ser distribuída: "))
        beneficiario = input("Digite o nome do beneficiário: ")
        distribuir_alimento(nome, quantidade, beneficiario)
        print()

    elif opcao == "6":
        relatorio_proximos_vencimento()
        print()

    elif opcao == "7":
        nome = input("Digite o nome do alimento que deseja consultar: ").upper()
        consultar_alimento(nome)
        print()

    elif opcao == "0":
        escolha = input("Digite [S] para sair e [M] para voltar ao menu: ").upper()
        if escolha == "S":
            break
        else:
            continue

    else:
        print("Opção inválida. Digite novamente.")
        print()
