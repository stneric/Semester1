
#include <stdio.h>
#include <stdlib.h>

typedef struct Liste{

	int wert;
	struct Liste* next_elem;

}Liste;


int main(void) {

	Liste* head = NULL;

	Liste* elem1 = malloc(sizeof(Liste));
	Liste* elem2 = malloc(sizeof(Liste));
	Liste* elem3 = malloc(sizeof(Liste));
	Liste* elem4 = malloc(sizeof(Liste));

	elem1->wert = 1;
	elem1->next_elem = head;

	head = elem1;

	elem2->wert = 2;
	elem2->next_elem = head;

	head = elem2;

	elem3->wert = 3;
	elem3->next_elem = head;

	elem3 = head;

	elem4->wert = 4;
	elem4->next_elem = head;

	elem4 = head;

	printf("%d, %d, %d, %d", elem1->wert, elem2->wert, elem3->wert, elem4->wert);

	return EXIT_SUCCESS;
}
