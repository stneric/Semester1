#include <stdio.h>
#include <stdlib.h>

struct spielen {
	int a;
	int b;
	int c;
	char d;
	char e;
	char f;
	char g;
	char h;
};



int main(void) {

	
	int *pointer = malloc(sizeof(int)); //Pointer hat die Größe eines Integers
	*pointer = 43; //Pointer hat den Wert 43

	printf("%p, %d\n", pointer, *pointer);
	// Ausgabe:   "0x55f64f8dc2a0, 43"
	
	struct spielen* spiel1 = malloc(sizeof(struct spielen));
	spiel1->a = 100;
	//Im Struct Spiel1 auf (->) a den Wert 100 speichern
	
	printf("a = %d\n", spiel1->a);
	//Ausgabe: "a = 100"

    
    spiel1->f = 'j';
    printf("%c", &spiel1->f);

	return EXIT_SUCCESS;
}