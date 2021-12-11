
# A function is a collection of instructions

def function1():
    print("def = definieren")
    print("function1 ist der Name der Funktion")

# die print lines in der funktion werden definiert aber nicht ausgegeben.

print("das ist außerhalb der Funktion")

# hier wird die Funktion ausgegeben

function1()

def function2(x):   #def Funktion mit Wert x, für später
    return 2*x      #return 2 mal "x"

#wir können die Funktion rufen mit:

a = function2(4)    #4 = x. Also 4*2 = 8, wird als Wert für a gespeichert

print(a)

# a hat nun den Wert "8"

b = function2(9)

print(b)

# d = function2() -> Error weil kein Wert gegeben ist.

# man kann es auch mit 2 Werten machen

def function3(x, y):
    return x + y 

e = function3(1, 2)

print(e)    


def function4(x):
    print(x)
    print("still in this function")
    return 3*x

f = function4(4)    
print(f)

def function5(some_argument):
    print(some_argument)
    print("weeeeeeee")

function5(4)    
function5("hell")   # "some_function" kann eine Variable oder etwas anderes sein. 




'''
Created on 02.11.2021

@author: ericstein
'''
