# Dado um sinal aritmético e dois valores, calcular a operação desejada
# EXEMPLO: Se o usuário digitar + 3 7 , imprimir: 10

calc = str(input("Digite um sinal aritmético: "))
n1 = float(input("Digite o primeiro valor: "))
n2 = float(input("Digete o segundo valor"))
match calc:
    case "+":
        x = n1 + n2
        print(f"O Resultado da soma é: {x:.2f}")
    case "-":
        x = n1 - n2
        print(f"O Resultado da subtração é: {x:.2f}")
    case "*":
        x = n1 * n2
        print(f"O Resultado da multiplicação é: {x:.2f}")
    case "/":
        if n2 != 0:
            x = n1 / n2
            print(f"O Resultado da divisão é: {x:.2f}")
        else:
            print("ERRO")
    case "//":
        if n2 != 0:
            x = n1 // n2
            print(f"O Resultado inteiro da divisão é: {x}")
        else:
            print("ERRO")
    case "%":
        if n2 != 0:
            x = n1 % n2
            print(f"O Módulo da divisão é: {x}")
        else:
            print("ERRO")
    case "**":
        x = n1 ** n2
        print(f"O Resulstado da potência é: {x:.2f}")
