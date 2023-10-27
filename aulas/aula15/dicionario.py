import os

# Criar um dicionário vazio:
dic = {}

# Dicionário com valores padrão:
contato = {
    'nome': 'Pedro Daniluz',
    'idade': 19,
    'email': 'pedrodaniluz04@gmail.com',
    'telefone': '11940188939'
}

# Acessar dados em dicionários:
print(f"Nome: {contato['nome']}")

# Inserir dados em dicionários:
contato['instagram'] = input("Instagram: ")
print(contato)


# Exibir de maneira ordenada:
def exibe_dicionario(c: dict):
    for chave in c:
        tamanho = len(chave)
        tamanho = 20 - tamanho
        pontos = "." * tamanho
        print(f"{chave}{pontos}: {c[chave]}")


exibe_dicionario(contato)
