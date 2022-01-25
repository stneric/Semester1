#include <stdlib.h>
#include <stdio.h>

typedef struct liste{
    int value;
    struct liste* nextelem;
}liste;



int main(void){

    liste* firstblock = malloc(sizeof(liste));
    liste* secondblock = malloc(sizeof(liste));
    liste* thirdblock = malloc(sizeof(liste));

    liste* head = NULL;

    firstblock->value = 12;
    firstblock->nextelem = head;

    head = firstblock;


    secondblock->value = 23;
    secondblock->nextelem = head;

    head = secondblock;

    
    thirdblock->value = 44;
    thirdblock->nextelem = head;

    head = thirdblock;

    printf("%d \n%d \n%d", firstblock->value, secondblock->value, thirdblock->value);



    return EXIT_SUCCESS;
}