#include <stdlib.h>
#include <stdio.h>
#include <string.h>
#include "test.h"

int main(void){

    test* new = malloc(sizeof(test));
    new->a = 12;

    printf("%d\n", new->a);

    abigs *neues = malloc(sizeof(abigs));

    neues->b = 2;
    neues->c = 'e';
    strcpy(neues->dd, "testing");

    printf("%d, %c, %s", neues->b, neues->c, neues->dd);

    return EXIT_SUCCESS;
}