# komplexe if else Abfragen umgehen
eingabe_erflogreich = False
while not eingabe_erflogreich:

    eingabe = input("bitte zwei Zahlen hintereinander durch Leerzeichen getrennt eingeben: ")


    try:
        a, b = eingabe.split() #teilt die Eingabe in zwei Variablen ein (String aufteilen)
    #a, b = eingabe.split(",") durch Kommata getrennt -> macht Kommata weg
        try:
            erg = int(a) + int(b)
            print(f" a = {a}, b = {b} und die Summe der beiden ist {erg}")
            eingabe_erfolgreich = True
        except:
            print("Zwei Zahlen!")
            
    except ValueError: # mach genau diese Meldung wenn ein ValueError auftritt
        print("Es wurden nicht zwei Werte durch Leerzeichen getrennt eingegeben")

    finally:
        print("Done!")

    try:
        assert(int(a) < 10)
    except AssertionError:
        print("a muss kleiner 10 sein")

