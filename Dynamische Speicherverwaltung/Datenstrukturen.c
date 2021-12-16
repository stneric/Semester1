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

	int *speicher = malloc(100); // 100 Byte

	printf("%p\n", speicher);

	printf("%i\n", sizeof(int));
	printf("%i\n", sizeof(char));
	printf("%i\n", sizeof(struct spielen));

	printf("%i\n", sizeof(speicher));

	struct spielen* spielfeld = malloc(sizeof(struct spielen) * 100);

	struct spielen spiel_auf_stack;
	spiel_auf_stack.a = 10;
	printf("%i\n", spiel_auf_stack.a);

	spielfeld[1].a = 7;
	printf("%i\n", spielfeld[1].a);

	struct spielen* spiel_einzel = malloc(sizeof(struct spielen));
	spiel_einzel->b = 42;
	printf("%i\n", spiel_einzel->b);

	int* heapspeicher = malloc(4);
	printf("%p\n", heapspeicher);
	*heapspeicher = 42;
	printf("%p %i\n", heapspeicher, *heapspeicher);

	return EXIT_SUCCESS;
}