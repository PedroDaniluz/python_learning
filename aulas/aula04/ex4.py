# Dado os dígitos da placa de um carro, exibir o dia do rodízio.

p = input("Digite os valores ")

p = p[:4]
ultimo = p[-1]
match ultimo:
    case "1":
        print("Segunda-Feira")
    case "2":
        print("Segunda-Feira")
    case "3":
        print("Teça-Feira")
    case "4":
        print("Teça-Feira")
    case "5":
        print("Quarta-Feira")
    case "6":
        print("Quarta-Feira")
    case "7":
        print("Quinta-Feira")
    case "8":
        print("Quinta-Feira")
    case "9":
        print("Sexta-Feira")
    case "0":
        print("Sexta-Feira")
    case _:
        print("ERRO")
