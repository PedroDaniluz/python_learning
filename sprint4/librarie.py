import os
from datetime import date
from dafault_data import *


def menu():
    os.system('cls' if os.name == 'nt' else 'clear')
    print(" ╔════════════════ MENU ══════════════════╗")
    print(" ║ 1 - Cadastrar Veículo                  ║")
    print(" ║ 2 - Registrar Manutenção               ║")
    print(" ║ 3 - Exibir Registros e Previsões       ║")
    print(" ║ 0 - Sair                               ║")
    print(" ╚════════════════════════════════════════╝")


def menu_record():
    os.system('cls' if os.name == 'nt' else 'clear')
    print(" ╔══════════════ MODALIDADE ═══════════════╗")
    print(" ║ 1 - Alinhamento                         ║")
    print(" ║ 2 - Balanceamento                       ║")
    print(" ║ 3 - Cambagem                            ║")
    print(" ║ 4 - Bateria                             ║")
    print(" ║ 5 - Freios                              ║")
    print(" ║ 6 - Pneus                               ║")
    print(" ║ 7 - Óleo                                ║")
    print(" ║ 8 - Velas                               ║")
    print(" ║ 9 - Filtro                              ║")
    print(" ║ 0 - Sair                                ║")
    print(" ╚═════════════════════════════════════════╝")


def add_vehicle(register: dict, model: str, brand: str, year: str):
    register['Modelo'] = model
    register['Marca'] = brand
    register['Ano'] = year


def add_maintenance(register: dict, provider: str, date: str, km: float):
    register['Provedor'] = provider
    register['Data'] = date
    register['Quilometragem'] = km


def forecast(register: dict, km_to_new: int) -> str:
    if register['Provedor'] == "SEM DADOS":
        return "SEM DADOS"
    else:
        next_maintenance = float(register['Quilometragem']) + km_to_new
        return f"{next_maintenance} KM"


def record_options(register: dict):
    provider = input("Digite a empresa responsável pela manutenção: ")

    # Validação do campo data
    data = input("Digite a data da manutenção (DD/MM/AAAA): ")
    while True:
        if len(data.split("/")) != 3:
            data = input("Digite uma data válida (DD/MM/AAAA): ")
        else:
            day, month, year = data.split("/")
            if not day.isnumeric() or not month.isnumeric() or not year.isnumeric():
                data = input("Digite uma data válida (DD/MM/AAAA): ")
            else:
                if not 1900 < int(year) <= date.today().year:
                    data = input("Digite uma data com ano válido (DD/MM/AAAA): ")
                elif not 0 < int(month) <= 12:
                    data = input("Digite uma data com mês válido (DD/MM/AAAA): ")
                elif not 0 < int(day) <= 31:
                    data = input("Digite uma data com dia válido (DD/MM/AAAA): ")
                elif int(year) == date.today().year:
                    if not 0 < int(month) <= date.today().month:
                        data = input("Digite uma data com mês válido (DD/MM/AAAA): ")
                    elif int(month) == date.today().month:
                        if not 0 < int(day) <= date.today().day:
                            data = input("Digite uma data com dia válido (DD/MM/AAAA): ")
                        else:
                            break
                else:
                    break

    # Validação do campo Km
    km = input("Digite a quilometragem do veículo na data da manutenção: ")
    while not km.isnumeric() or float(km) < 0:
        km = input("Digite um valor válido para quilometragem: ")

    # Função em si, atualizando as informações
    add_maintenance(register, provider, data, float(km))


def format_print(text: str, char: str, char_start: str, char_end):
    # Recebe um nome para cabeçalho, um caractere de espaçamento, um de início e um de fim. Criando uma linha formatada.
    len_text = len(text)
    if len_text % 2 != 0:
        len_text += 1
        text = f"{text} "
    qnt_barras = 25 - (len_text // 2)
    barras = char * qnt_barras
    return f" {char_start}{barras} {text} {barras}{char_end}"


def print_records(table: list):
    # Percorre uma tabela com todos os dicionários, formatando e imprimindo cada informação
    for i in range(0, len(table), 1):
        print(format_print(table[i]['Nome'], "═", "╔", "╗"))
        print(f"    Provedor: {table[i]['Provedor']}")
        print(f"    Data: {table[i]['Data']}")
        print(f"    Quilometragem: {table[i]['Quilometragem']} KM")
        print(f"    Próxima manutenção: {forecast(table[i], table[i]['Proxima'])}\n")


def save():
    with open("data.txt", "w", encoding="utf-8") as data:
        data.write(
            f"{my_vehicle['Modelo']}|{my_vehicle['Marca']}|{my_vehicle['Ano']}.\n"
            f"{alignment_hist['Provedor']}|{alignment_hist['Data']}|{alignment_hist['Quilometragem']}.\n"
            f"{balancing_hist['Provedor']}|{balancing_hist['Data']}|{balancing_hist['Quilometragem']}.\n"
            f"{camber_hist['Provedor']}|{camber_hist['Data']}|{camber_hist['Quilometragem']}.\n"
            f"{battery_hist['Provedor']}|{battery_hist['Data']}|{battery_hist['Quilometragem']}.\n"
            f"{breaks_hist['Provedor']}|{breaks_hist['Data']}|{breaks_hist['Quilometragem']}.\n"
            f"{tires_hist['Provedor']}|{tires_hist['Data']}|{tires_hist['Quilometragem']}.\n"
            f"{oil_hist['Provedor']}|{oil_hist['Data']}|{oil_hist['Quilometragem']}.\n"
            f"{sparkplug_hist['Provedor']}|{sparkplug_hist['Data']}|{sparkplug_hist['Quilometragem']}.\n"
            f"{filters_hist['Provedor']}|{filters_hist['Data']}|{filters_hist['Quilometragem']}.\n"
            )


def load_hist(hist: dict) -> None:
    with open("data.txt", "r", encoding="utf-8") as cont:
        data = cont.readlines()
        hist['Provedor'] = data[hist['Linha']].split('.')[0].split('|')[0]
        hist['Data'] = data[hist['Linha']].split('.')[0].split('|')[1]
        hist['Quilometragem'] = data[hist['Linha']].split('.')[0].split('|')[2]


def load():
    with open("data.txt", "r", encoding="utf-8") as cont:
        data = cont.readlines()
        my_vehicle['Modelo'] = data[my_vehicle['Linha']].split('.')[0].split('|')[0]
        my_vehicle['Marca'] = data[my_vehicle['Linha']].split('.')[0].split('|')[1]
        my_vehicle['Ano'] = data[my_vehicle['Linha']].split('.')[0].split('|')[2]
        load_hist(alignment_hist)
        load_hist(balancing_hist)
        load_hist(camber_hist)
        load_hist(battery_hist)
        load_hist(breaks_hist)
        load_hist(tires_hist)
        load_hist(oil_hist)
        load_hist(sparkplug_hist)
        load_hist(filters_hist)


def load_database():
    try:
        load()
    except FileNotFoundError:
        arq = open("data.txt", "w")
        arq.close()
