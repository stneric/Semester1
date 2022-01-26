#include <stdlib.h>
#include <stdio.h>
#include <string.h>

//a)
typedef struct a4{

    int zahl;
    char buchstabe;
    float zahl2;

}a4;


int main(void){

    struct a4 arr_a4[5];

    a4* a  = malloc(sizeof(a4));

    a->zahl = 1;
    a->buchstabe = 'a';
    a->zahl2 = 1.1;



    FILE *filepointer;


    filepointer = fopen("test2.txt", "w");


    if (filepointer == NULL){
        printf("Fehler beim öffnen der Datei");
        return -1;
    }


    fprintf(filepointer, "test\n");




    return EXIT_SUCCESS;
}