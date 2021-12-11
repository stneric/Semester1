
feld = [10,11,12,13,14,15,16,17,18,19]

print(feld[0])
print(feld[-1])
print(feld[3])

for i in range(len(feld)):
    if feld[i] == 15:
        feld[i] = 30
    
for i in range(len(feld)):
    print(feld[i])

print(feld[:5])
print(feld[::-1])
print(feld[3:8:2])

def summeberechnen(feld):
    erg = 0

    for i in range(len(feld)):
        erg = erg + feld[i]
    
    return erg


print("Summe = ",summeberechnen(feld))


def pow(zahl, exponent, erg):

    if exponent == 0:
        exponent = 2

    for i in range(1, exponent+1):
        erg = erg * zahl

    print(erg)

erg = 1
pow(2,0,erg)


def root(e,n):
    if n < 0:
        return 1

    else:
        pass

