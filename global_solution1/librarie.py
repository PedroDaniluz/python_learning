import datetime

alimentos = []


def cadastrar_alimento(nome, categoria, data_validade, quantidade):
    alimento = {
        'nome': nome,
        'categoria': categoria,
        'data_validade': data_validade,
        'quantidade': quantidade
    }
    alimentos.append(alimento)


def atualizar_alimento(nome, quantidade):
    for alimento in alimentos:
        if alimento['nome'] == nome:
            alimento['quantidade'] = quantidade
            break


def remover_alimento(nome):
    for alimento in alimentos:
        if alimento['nome'] == nome:
            alimentos.remove(alimento)
            break


def listar_alimentos():
    for alimento in alimentos:
        print(f"Nome: {alimento['nome']}")
        print(f"Categoria: {alimento['categoria']}")
        print(f"Data de validade: {alimento['data_validade']}")
        print(f"Quantidade disponível: {alimento['quantidade']}")
        print()


def distribuir_alimento(nome, quantidade, beneficiario):
    for alimento in alimentos:
        if alimento['nome'] == nome:
            if alimento['quantidade'] >= quantidade:
                alimento['quantidade'] -= quantidade
                data_distribuicao = datetime.date.today()
                print(f"{quantidade} unidades de {alimento['nome']} foram distribuídas para "
                      f"{beneficiario} em {data_distribuicao}.")
            else:
                print(f"A quantidade de {alimento['nome']} disponível não é suficiente.")
            break


def relatorio_proximos_vencimento():
    data_atual = datetime.date.today()
    for alimento in alimentos:
        dias_restantes = (alimento['data_validade'] - data_atual).days
        if dias_restantes < 0:
            dias_restantes2 = - dias_restantes
            print(f"O alimento {alimento['nome']} venceu há {dias_restantes2} dias.")
        elif dias_restantes <= 7:
            print(f"O alimento {alimento['nome']} vence em {dias_restantes} dias.")


def consultar_alimento(nome):
    for alimento in alimentos:
        if alimento['nome'] == nome:
            print(f"Nome: {alimento['nome']}")
            print(f"Categoria: {alimento['categoria']}")
            print(f"Data de validade: {alimento['data_validade']}")
            print(f"Quantidade disponível: {alimento['quantidade']}")
            return
    print("Alimento não encontrado.")