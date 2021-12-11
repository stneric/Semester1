
def function(x):
    y = (x**2)-3*x**2
    return y


def rekursiv(start, stop, step):

    if start >= stop:
        return -1

    else:
        
        #x definieren und schritt durch zwei
        mid = start + (step/2)

        # in die funktion und mal y
        erg = abs(function(mid) * step)
        start = mid
        rekursiv(start,stop,step)
        erg = erg+erg

    return erg



start = -2
stop = 2
step = 0.5

print(rekursiv(start,stop,step))


