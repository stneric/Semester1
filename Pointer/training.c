#include <stdlib.h>
#include <string.h>
#include <stdio.h>

typedef struct{
    int number;
    char character;
    char stringarray[100];
}test;



int main(void){

    test* newstruct = malloc(sizeof(test));

    newstruct->number = 22;
    newstruct->character = 'N';
    strcpy(newstruct->stringarray, "Moin Meister");

    printf("%d, %c, %s", newstruct->number, newstruct->character, newstruct->stringarray);



    return EXIT_SUCCESS;
}