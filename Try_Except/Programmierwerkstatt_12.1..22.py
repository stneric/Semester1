# komplexe if else Abfragen umgehen

eingabe = input("bitte zwei Zahlen hintereinander durch Leerzeichen getrennt eingeben: ")

try:
    a, b = eingabe.split() #teilt die Eingabe in zwei Variablen ein (String aufteilen)
#a, b = eingabe.split(",") durch Kommata getrennt -> macht Kommata weg
    erg = int(a) + int(b)

except ValueError: # mach genau diese Meldung wenn ein ValueError auftritt
    print("Es wurden nicht zwei Werte durch Leerzeichen getrennt eingegeben")

print(f" a = {a}, b = {b} und die Summe der beiden ist {erg}")