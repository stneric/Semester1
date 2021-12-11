'''
Created on 02.11.2021

@author: ericstein
'''

# print("Hello World") ist eine Funktion (Print) und ein String "Hello World"
# Zahlen müssen nicht in "" geschirieben sein.

#a = 1       # a ist eine Variable
#print(a)    # Gibt "1" aus

#f = a       # f hat den Wert 1, nicht den Wert a
#print(f)    


#SWAPPING TWO VARIABLES

v1 = "first string"
v2 = "second string"

temp = v1   # Temporäre Variable
v1 = v2     # "first string" ist jetzt "second string"
v2 = temp   # "second string" ist jetzt "first string"

print(v1)   # Test ob es wirklich gewechselt wurde
print(v2)

#SWITCH IT BACK

temp = v2
v2 = v1
v1 = temp

print(v1)   # Test ob es wirklich wieder zurück gewechselt wurde 
print(v2)

