#include <stdio.h> 
#include <stdlib.h>
#include <asstert.h>

// Baum 

typedef struct bbaum{
    int wert;
    struct baum*lk;
    struct baum*rk;
}bbaum;

bbaum* erzeuge:knoten(int wert){
    bbaum* k = malloc(sizeof(baum));
    if(k == NULL) {
        //Fehlerbehandlung
    }
    assert(k != NULL); 

    k-> wert
}

// um zu checken welchen Knoten man schon "gesehen" hat. Entweder mit einem Struct in dem man sich
// das speichern kann, oder man setzt die "Farbe" auf rot (z.B.) wenn man noch nicht drin war etc.

void print_tiefensuche_baum_praefix(bbaum* wurzel){ //Praefix = Ausgabe vor Funktion 

    if(wurzel == NULL){                 // NULL == nicht existent, kein Knoten da.
        return;
    }
    printf("%i\n", wurzel-> wert);
    print_tiefensuche_baum_praefix(wurzel->lk); // "->" Zugriff auf Struct
    print_tiefensuche_baum_praefix(wurzel->rk);
}

void print_tiefensuche_baum_postfix(bbaum* wurzel){ //Postfix = Aufgabe nach Funktion (dreht quasi Praefix um)
                                                    // braucht man immer dann, wenn man z.B. was zsm rechnet 
                                                    // erst wird gerechnet, dann ausgegeben also:
                                                    // (1+2) * (2+3) != Ausgabe: (3) * (5) sondern Ausgabe: 15
                                                    // geht also nicht schrittweise durch di eGleichung durch

    if(wurzel == NULL){                 // NULL == nicht existent, kein Knoten da.
        return;
    }
    print_tiefensuche_baum_postfix(wurzel->lk);
    print_tiefensuche_baum_postfix(wurzel->rk);
    printf("%i\n", wurzel-> wert);
}

void print_tiefensuche_baum_infix(bbaum* wurzel){ //Infix = Aufgabe in mitten Funktion - braucht man selten

    if(wurzel == NULL){                 // NULL == nicht existent, kein Knoten da.
        return;
    }
    print_tiefensuche_baum_infix(wurzel->lk);
    
    printf("%i\n", wurzel-> wert);

    print_tiefensuche_baum_infix(wurzel->rk);
}

int main(void) {
    bbaum* wurzel = erzeuge_knoten(42);
    printf("%i\n", wurzel->wert);
    fuege_wert_ein(1,wurzel);
    fuege_wert_ein(3,wurzel);
    fuege_wert_ein(50,wurzel);
    fuege_wert_ein(0,wurzel);

    print_tiefensuche_baum_praefix(wurzel);
    print_tiefensuche_baum_postfix(wurzel);
    print_tiefensuche_baum_infix(wurzel);

    return EXIT_SUCCESS;
}