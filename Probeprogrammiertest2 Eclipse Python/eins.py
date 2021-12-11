from matplotlib.pyplot import step



# A1 

#a)

feld = [10,11,12,13,14,15,16,17,18,19]

#b)

print("Erstes Element", feld[0])
print("Letztes Element", feld[-1])
print("Element an Index 3", feld[3])

#c)

feld[4] = 20
print(feld)

#d)

feld[1], feld[7] = feld[7], feld[1]
print(feld)

#e)

for element in feld:
    print(element)
    

#B1

#a)

print(feld[:5])

#b)

print(feld[3:8:2])

#c)

print(feld[::-1])

#A2 Rekursion

#a)
def f(x):
    y = (0.5*x**4)-2*x**2+(x-1)
    return y
    
    
#b)

def flaeche(start,stop,step):
    
    if start > stop:
        return 1
    
    else:
        start = start+step
        
                    

print(flaeche(-2,2,1))
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    