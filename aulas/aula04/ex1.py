# Dado um valor numérico, mostrar o dia da semana correspondente.
# EXEMPLO: Se o usuário digitar 5, imprimir: 'Quinta-Feira'

dia = int(input("Digite um número: "))

match dia:
    case 1:
        print("Domingo")
    case 2:
        print("Segunda")
    case 3:
        print("Terça")
    case 4:
        print("Quarta")
    case 5:
        print("Quinta")
    case 6:
        print("Sexta")
    case 7:
        print("Sábado")
    case _:
        print("ERRO")