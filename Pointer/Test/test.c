#include <stdio.h>
#include <stdlib.h>
#include <string.h>

typedef struct test{

    int ganzzahl;
    int array[];

}test;


int main(void){

    test* testing = malloc(sizeof(test));

    testing->ganzzahl = 12;

    testing->array[1] = 1;
    testing->array[2] = 2;
    testing->array[3] = 3;
    testing->array[4] = 4;

    for(int i=0; i>5; i++){
        printf("%d, ", testing->array[i]);
    }

    return EXIT_SUCCESS;
}