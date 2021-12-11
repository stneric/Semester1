
def rechnung(x):
    y = (x**2)-3*x**2
    return y


def ann(lgrenze, rgrenze, schritt):

    erg = 0

    while lgrenze < rgrenze:

        mitte = lgrenze + (schritt/2)

        if mitte < 0 or schritt < 0:
            erg += rechnung(mitte) * schritt *-1

        else:
            erg += rechnung(mitte) * schritt

        lgrenze += schritt
    return erg







print(ann(-2,2,0.5))

