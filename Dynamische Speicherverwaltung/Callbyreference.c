def tu_was(listename):
    listename.append(4)

liste = [1, 2, 3]
print(liste)
tu_was(liste)
print(liste)


def tu_was_int(zahl):
    zahl += 1
    print(zahl, " in Funktion")

zahl = 0
print(zahl)
tu_was_int(zahl)
print(zahl)