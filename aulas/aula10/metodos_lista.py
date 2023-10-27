cavaleiros_jedi = ["Obi-Wan Kenobi", "Mace Windu", "Mestre Yoda", "Luke Skywalker", "Anakin Skywalker"]
print(f"A lista original é \n{cavaleiros_jedi}")

# lista.append(elemento) - Adiciona um novo elemento no final da lista
cavaleiros_jedi.append("Mestre Yoda")
print(f"Após a adição do elemento Mestre Yoda utilizando o append, a lista é \n{cavaleiros_jedi}")

# lista.index(elemento) - Retorna a posição do elemento na lista
print(f"O índice do elemento Mace Windu é {cavaleiros_jedi.index('Mace Windu')}")

# lista.insert(elemento, posicao) - Adiciona um elemento em uma posição definida da lista
cavaleiros_jedi.insert(1, "Rey")
print(f"Após a adição do elemento Rey na posição 1 utilizando o insert, a lista é \n{cavaleiros_jedi}")

# lista.count(elemento) - Retorna a quantidade de vezes que um elemento apareceu na lista
print(f"A contagem do elemento Mestre Yoda é {cavaleiros_jedi.count('Mestre Yoda')}")

# lista.pop() - Remove o último elemento da fila
cavaleiros_jedi.pop()
print(f"Após o uso do pop, a lista é \n{cavaleiros_jedi}")

# lista.pop(posicao) - Remove o elemento na posição dada como parâmetro
cavaleiros_jedi.pop(0)
print(f"Após o uso do pop com o índice 0, a lista é \n{cavaleiros_jedi}")

# lista.reverse() - Inverte a ordem dos elementos de uma lista
cavaleiros_jedi.reverse()
print(f"Após o uso do reverse, a lista é \n{cavaleiros_jedi}")

# lista.sort() - Ordena a lista em ordem crescente
cavaleiros_jedi.sort()
print(f"Após o uso do sort, a lista é \n{cavaleiros_jedi}")

# lista.sort(reverse=True) - Ordena a lista em ordem decrescente
cavaleiros_jedi.sort(reverse=True)
print(f"Após o uso do sort(reverse=True), a lista é \n{cavaleiros_jedi}")
