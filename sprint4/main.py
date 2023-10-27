from librarie import *
from dafault_data import *

while True:
    load_database()
    # O procedimento menu() imprime as opções iniciais na tela:
    menu()
    opc = input("Escolha uma opção: ")
    # Validação da entrada do usuário:
    while not opc.isnumeric() or int(opc) < 0 or int(opc) > 3:
        menu()
        opc = input("Escolha um valor válido: ")
    else:
        # Após passar do validador, realizar função de acordo com a opçao escolhida
        match int(opc):
            case 1:
                # Inserir dados iniciais do veículo, e atualizar o dicionário padrão
                brand = input("Digite a marca do veículo: ")
                model = input("Digite o modelo do veículo: ")
                year = input("Digite o ano do veículo: ")
                while not year.isnumeric() or int(year) < 1900 or int(year) > date.today().year:
                    year = input("Digite um ano válido: ")
                add_vehicle(my_vehicle, model, brand, year)
                save()
            case 2:
                # Verificar se o veículo foi adicionado
                os.system('cls' if os.name == 'nt' else 'clear')
                empty = False
                if my_vehicle['Marca'] == "SEM DADOS":
                    empty = True
                    print("Primeiro insira as informações do veículo")
                    input("Digite algo para continuar: ")

                # Inserir dados de manutenção, e atualizar o dicionário padrão
                while not empty:
                    # O procedimento menu_record() imprime as opções de registro de manutenção:
                    menu_record()
                    field = input("Escolha uma opção: ")
                    # Validação da entrada do usuário:
                    while not field.isnumeric() or int(field) < 0 or int(field) > 9:
                        menu_record()
                        field = input("Digite um valor válido: ")
                    else:
                        # Após passar do validador, realizar função de acordo com a opçao escolhida
                        # A rotina record_options(), solicita dados ao usuário e atualiza os dicionários padrões
                        match int(field):
                            case 1:
                                record_options(alignment_hist)
                            case 2:
                                record_options(balancing_hist)
                            case 3:
                                record_options(camber_hist)
                            case 4:
                                record_options(battery_hist)
                            case 5:
                                record_options(breaks_hist)
                            case 6:
                                record_options(tires_hist)
                            case 7:
                                record_options(oil_hist)
                            case 8:
                                record_options(sparkplug_hist)
                            case 9:
                                record_options(filters_hist)
                            case 0:
                                break
                save()
            case 3:
                # Verificar se o veículo foi adicionado
                os.system('cls' if os.name == 'nt' else 'clear')
                if my_vehicle['Marca'] == "SEM DADOS":
                    print("Primeiro insira as informações do veículo")
                    input("Digite algo para continuar: ")

                # Exibir as informações do veículo e o histórico de manutenção, além da previsão das próximas
                else:
                    # A função format_print() serve para formatar a impressão do cabeçalho, no caso, somente espaçamento
                    head = f"VEÍCULO: {my_vehicle['Marca'].upper()} {my_vehicle['Modelo'].upper()}"
                    print(f"\n{format_print(head, ' ', ' ', ' ')}\n")

                    # A função print_records() recebe uma lista com todas os dicionários para formatação
                    print_records([alignment_hist, balancing_hist, camber_hist, battery_hist, breaks_hist, tires_hist,
                                   oil_hist, sparkplug_hist, filters_hist])
                    input("Pressione qualquer tecla para voltar: ")
                save()
            case 0:
                break
