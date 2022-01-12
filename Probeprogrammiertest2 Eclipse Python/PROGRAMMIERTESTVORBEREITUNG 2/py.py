
A = [0,1,2,3,4,5,6,7,8,9,10]


print(A[::1])

print(A[::-1])
print(A[-1])
print(A[:5:-1])

#Fakultaet !n

def iterativ(n):

    erg = 1
    
    while(n>1):
            erg = erg*n
            n = n-1
    
    return erg


def rekursiv(n, erg):
    if n == 1:
        return 0

    else:
        erg = erg+n
        rekursiv(n-1,erg)
        
    print(erg)


    




erg = 1
rekursiv(5,erg)
print(iterativ(5))