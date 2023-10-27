def interv(n1, n2, p):
    x = 0

    if p == "A":
        if n1 < n2:
            dif = (n2 - 1) - n1
            while x < dif:
                print((n1 + 1) + x)
                x += 1

        elif n2 < n1:
            dif = (n1 - 1) - n2
            while x < dif:
                print((n2 + 1) + x)
                x += 1

        else:
            print()

    if p == "F":
        if n1 < n2:
            dif = n2 - n1
            while x <= dif:
                print(n1 + x)
                x += 1

        elif n2 < n1:
            dif = n1 - n2
            while x <= dif:
                print(n2 + x)
                x += 1

        else:
            print()


interv(20, 20, "A")
