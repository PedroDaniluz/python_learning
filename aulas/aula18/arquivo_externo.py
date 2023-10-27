# Manipulação de arquivos texto

"""
Modos de abertura:
w   - write | Escrita
r   - read  | Leitura
x   - write | Para arquivos inexistentes
a   - append| Edição de arquiv
+   - Abertura para edição e leitura juntos
"""

# Função open() -> Possibilita a abertura de um arquivo
# Sintaxe: <objeto> = open("nome_arquivo","forma_abertura")

import os

os.system("cls")
# Gravando dados no arquivo
arq = open("arquivo.txt", "w", encoding="utf-8")
arq.write("Gravação da linha 1\n")  # write escreve uma linha no arquivo
arq.write("Gravação da linha 2\n")  # write escreve uma linha no arquivo
arq.write("Gravação da linha 3\n")  # write escreve uma linha no arquivo
arq.close()  # close fecha o arquivo
print("Arquivo gravado")

# recuperando dados do arquivo
print("Antes...")
arq = open("arquivo.txt", "r", encoding="utf-8")
print(arq.read())  # read lê o arquivo na integra
arq.close()  # close fecha o arquivo

# Editar um arquivo
arq = open("arquivo.txt", "a", encoding="utf-8")
arq.write("Adicionando uma linha\n")
arq.close()

print("Depois...")
arq = open("arquivo.txt", "r", encoding="utf-8")
print(arq.read())  # read lê o arquivo na integra
arq.close()  # close fecha o arquivo

# Abrindo em modo escrita x
arq = open("arquivo2.txt", "x", encoding="utf-8")
arq.write("Adicionando uma linha\n")
arq.close()

arq = open("arquivo3.txt", "w+", encoding="utf-8")
arq.write("Gravando no arquivo 3\n")
arq.seek(4)
print(arq.read())
arq.close()

arq = open("arquivo4.txt", "w+", encoding="utf-8")
arq.write("Gravando linha 1\n")
arq.write("Gravando linha 2\n")
arq.write("Gravando linha 3\n")
arq.seek(0)
# Lendo linhas
print(arq.readline(), end="")  # Lê a linha onde está o cursor
print(arq.readline(), end="")  # Lê a linha onde está o cursor
print(arq.readline(), end="")  # Lê a linha onde está o cursor
arq.close()

# Exercício: Ler somente a linha 2
# Resolução com gerenciador de contexto with
with open("arquivo4.txt", "w+", encoding="utf-8") as arq:
    arq.write("Gravando linha 1\n")
    arq.write("Gravando linha 2\n")
    arq.write("Gravando linha 3\n")
    arq.seek(0)
    # Lendo linhas
    lista = arq.readlines()  # Transforma em uma lista
    print(lista[1])
os.system("cls")

# Exercicios:
# 1. Contar quantas palavras há em um arquivo
# 2. Contar quantas vogais há em uma linha especificada pelo uuário
