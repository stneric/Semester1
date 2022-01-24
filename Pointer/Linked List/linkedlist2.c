#include <stdlib.h>
#include <stdio.h>

typedef struct llist{

    int number;
    struct llist* nelem;

}llist;


int main(void){

    llist* head = NULL;

    llist* elem1 = malloc(sizeof(llist));
    llist* elem2 = malloc(sizeof(llist));
    llist* elem3 = malloc(sizeof(llist));


    elem1->number = 1;
    elem1->nelem = head;

    head = elem1;

    elem2->number = 2;
    elem2->nelem = head;

    head = elem2;

    elem3->number = 100;
    elem3->nelem = head;

    head = elem3;

    printf("%d, %d, %d", elem1->number, elem2->number, elem3->number);

    return EXIT_SUCCESS;
}