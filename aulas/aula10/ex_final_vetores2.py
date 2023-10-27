# Fazer uma função chamada ‘conta_string(v)’ que conte quantos elementos strings existem em uma lista.
# Fazer uma função chamada ‘conta_boolean(v)’ que conte quantos elementos lógicos existem em uma lista.
# Fazer uma função chamada ‘conta_float(v)’ que conte quantos elementos float existem em uma lista.
# Fazer um procedimento chamado ‘copia_int(lista1, lista2)’ que copie para a lista 2 os elementos inteiros da lista 1

vet = ["Pedro", 21, True, "Mine", False, "17", 12, "19", 2, "1.2", "3.45", 12.2, "True", "pedrodaniluz.com.12.12.1"]
vet2 = ["PythonAmizade"]


def conta_string(v):
    som = 0
    for x in v:
        if type(x) == str:
            if x != "True" and x != "False":
                splited = x.split(".")
                tem_escrito = False
                for a in splited:
                    if not a.isnumeric():
                        tem_escrito = True
                if tem_escrito:
                    som += 1
    return som


def conta_string2(v):
    som = 0
    for x in v:
        if isinstance(x, str):
            if x != "True" and x != "False":
                splited = x.split(".")
                if any(not a.isnumeric() for a in splited):
                    som += 1
    return som


def conta_boolean(v):
    som = 0
    for x in v:
        if type(x) == bool:
            som += 1
        elif type(x) == str:
            if x == "True" or x == "False":
                som += 1
    return som


def conta_float(v):
    som = 0
    for x in v:
        if type(x) == float:
            som += 1
        elif type(x) == str:
            splited = x.split(".")
            if len(splited) == 2:
                if splited[0].isnumeric() and splited[1].isnumeric():
                    som += 1
    return som


def copia_int(v1, v2):
    for x in v1:
        if type(x) == int:
            v2.append(x)
        elif type(x) == str:
            if x.isnumeric():
                v2.append(int(x))
    return v2


print(conta_string2(vet))
print(conta_boolean(vet))
print(conta_float(vet))
print(copia_int(vet, vet2))
