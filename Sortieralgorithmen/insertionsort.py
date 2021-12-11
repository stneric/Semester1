

def insertionSort(liste):

    for index in range(1, len(liste)):      #zaehlt durch die ganze Liste
        aktuell = liste[index]              #aktueller Stand der Liste
        aktuellepos = index                 #aktueller Stand des index

        
        while aktuellepos > 0 and liste[aktuellepos - 1] >= aktuell:
            #solange der aktuelle index groesser als 0 ist und 
            #die Zahl am eben genannten index -1 groesser ist als
            #die Zahl an der Stelle index (aktuellepos),
            
            liste[aktuellepos] = liste[aktuellepos - 1]
            #dann wird die liste an der aktuellen position um eins 
            #nach links verschoben

            aktuellepos = aktuellepos -1
            #die aktuelle Position aendert sich dann um -1
            #und die Schleife wird wiederholt.

            #im ersten durchlauf isf der index = 1, somit wird die zweite
            #Zahl der Liste betrachtet, da die erste als schon sortiert
            #gilt

            #Der Index ist groesser als null und die liste ist an stelle 
            #index -1 gleich der liste an index 1

            #die Liste mit index 1 wird dann zu aktuell.

            #im zweiten Durchlauf ist der index dann 2 

        liste[aktuellepos] = aktuell

liste = [4, 7, 1, 0, 0, 5, 11, 42, 43, 2]

insertionSort(liste)
print("Sortierte Liste:", liste)
