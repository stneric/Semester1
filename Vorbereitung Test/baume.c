#include <string.h>
#include <stdio.h>
#include <stdlib.h>

typedef struct root_and_connect{

    int value;
    struct rac* leftchild;
    struct rac* rightchild;

}rac;



int main(void){

    struct rac* head = NULL;

    rac* first = malloc(sizeof(rac));
    rac* second = malloc(sizeof(rac));
    rac* third = malloc(sizeof(rac));


    first->value = 1;
    first->leftchild = head;
    first->rightchild = head;

    head = first;


    
    

    return EXIT_SUCCESS;
}