while True:
    print("""
    MENU
    1 - Intervalo
    2 - Intervalo Aberto e Fechado
    3 - Intervalo em ordem crescente ou decrescente
    0 - SAIR
    """)
    opcao = int(input("Escolha: "))
    match opcao:
        case 0:
            break
        case 1:
            print("INTERVALO")
            n1 = int(input("Primeiro número: "))  # 10
            n2 = int(input("Segundo número: "))  # 4
            if n1 > n2:
                aux = n1  # aux -> 10
                n1 = n2  # n1 -> 4
                n2 = aux  # n2 -> 10
            for i in range(n1, n2 + 1, 1):
                print(f"{i} ", end='')
        case 2:
            print("INTERVALO - Aberto e Fechado")
            n1 = int(input("Primeiro número: "))
            n2 = int(input("Segundo número: "))
            tipo = input("[A]berto ou [F]echado:")
            if n1 > n2:
                aux = n1  # aux -> 10
                n1 = n2  # n1 -> 4
                n2 = aux  # n2 -> 10
            if tipo == 'a' or tipo == "A":
                n1 = n1 + 1
                n2 = n2 - 1
            for i in range(n1, n2 + 1, 1):
                print(f"{i} ", end='')
        case 3:
            print("INTERVALO - Em ordem crescente ou decrescente")
            n1 = int(input("Primeiro número: "))
            n2 = int(input("Segundo número: "))
            if n1 < n2:
                for i in range(n1, n2 + 1, 1):
                    print(f"{i} ", end='')
            else:
                for i in range(n1, n2 - 1, -1):
                    print(f"{i} ", end='')
        case _:
            print("Opção inválida!")
