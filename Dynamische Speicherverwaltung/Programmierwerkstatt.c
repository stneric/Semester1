#include <stdio.h>
#include <stdlib.h>


struct zahlen {
	int a;
	int b;
};


int main(void) {

	int zahl = 42;
	int zahlenfeld[3] = {1, 2, 3};

	printf("%i ist gespeichert an Adresse %p\n", zahl, &zahl);
	printf("%i, %p\n", zahlenfeld[2], zahlenfeld);

	fflush(stdout);
	scanf("%i", &zahl);
	printf("%i ist gespeichert an Adresse %p\n", zahl, &zahl);

	fflush(stdin);
	fflush(stdout);

	char wort[10];
	scanf("%s", wort);
	printf("%s\n", wort);

	int* h_zahl = malloc(sizeof(int));
	printf("%i ist gespeichert an Adresse %p, h_zahl selbst steht an %p\n", *h_zahl, h_zahl, &h_zahl);
	*h_zahl = 42;
	printf("%i ist gespeichert an Adresse %p\n", *h_zahl, h_zahl);
	fflush(stdout);
	scanf("%i", h_zahl);
	printf("%i ist gespeichert an Adresse %p\n", *h_zahl, h_zahl);

	int* h_zahlenfeld = malloc(sizeof(int) * 3);
	h_zahlenfeld[0] = 1;
	h_zahlenfeld[1] = 2;
	h_zahlenfeld[2] = 3;
//	h_zahlenfeld[400] = 99;
	printf("%i, %p, %p\n", h_zahlenfeld[2], h_zahlenfeld,   &h_zahlenfeld);
	printf("%i, %p, %p\n", *h_zahlenfeld,   h_zahlenfeld,   &h_zahlenfeld);
	printf("%i, %p, %p\n", *h_zahlenfeld+1, h_zahlenfeld+1, &h_zahlenfeld);
	printf("%i, %p, %p\n", *h_zahlenfeld+2, h_zahlenfeld+2, &h_zahlenfeld);
//	printf("%i, %p, %p\n", *h_zahlenfeld+400, h_zahlenfeld+400, &h_zahlenfeld);
	free(h_zahlenfeld);

	char* h_wort = malloc(sizeof(char) * 10);
	scanf("%s", h_wort);
	printf("%s\n", h_wort);

	struct zahlen* schoene_zahlen = malloc(sizeof(struct zahlen));
	schoene_zahlen->a = 42;
	(*schoene_zahlen).b = 73;
	printf("Schöne Zahlen sind %i und %i.\n", (*schoene_zahlen).a, schoene_zahlen->b);

	struct zahlen* schoene_zahlen_array = malloc(sizeof(struct zahlen)*200);
	schoene_zahlen_array[100].a = 42;
	(*(schoene_zahlen_array+100)).b = 73;
	printf("Schöne Zahlen sind %i und %i.\n", schoene_zahlen_array[100].a, schoene_zahlen_array[100].b);

	return EXIT_SUCCESS;
}