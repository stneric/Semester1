#include <stdio.h>
#include <stdlib.h>
#include <struct.h>




void push(struct list* l,int val){ // neues List Element anlegen
    // Create Box
    elem* cur = malloc(sizeof(elem));
    
    //Insert to front of list
    if(l-> head == NULL){
        l->head = cur;
        l->tail = cur;
    } else{
        cur->next = head;
        l->head = cur;
    }
}


int main(int argc, char** argv){
		struct list grades;

		grades.head = NULL;
		grades.tail = NULL;

		print_list(&grades);
	}




