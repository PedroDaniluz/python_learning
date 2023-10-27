def converte_vogais_maiusculo(frase: str) -> str:
    new = []
    for a in frase:
        if a in ["a", "e", "i", "o", "u"]:
            new.append(a.upper())
        else:
            new.append(a)
    new_frase = "".join(new)
    return new_frase


# =============================================================


def isfloat(valor: str) -> bool:
    a = False
    x = valor.split(".")
    if len(x) == 2:
        if x[0].isnumeric() and x[1].isnumeric():
            a = True
        elif x[0].isnumeric() and x[1] == "":
            a = True
    return a
