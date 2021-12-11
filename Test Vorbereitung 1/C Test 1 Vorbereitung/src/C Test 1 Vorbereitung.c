/*
 ============================================================================
 Name        : C.c
 Author      : 
 Version     :
 Copyright   : Your copyright notice
 Description : Hello World in C, Ansi-style
 ============================================================================
 */

#include <stdio.h>
#include <stdlib.h>

int main(void) {

	int a = 22;
	int b = 6;
	printf("a hat den Wert %d, b hat den Wert %d\n", a, b);


	printf("a, also %d, geteilt durch b also %d ergibt: %d\n", a, b, a/b);


	printf("Der Rest, der beim Teilen von a und b entsteht, ist %d\n", a%b);




	if( a > b){
		printf("%d ist größer als %d\n", a, b);
	}
		else if ( a == b ){
				printf("%d ist gleichgroß wie %d\n", a, b);

		}
				else {
					printf("%d ist kleiner als %d \n", b, a);
				}

	int Wert = 0;

	printf("Welcher Wert soll geprüft werden?");
	scanf("%d", &Wert);

	if(Wert % 3 == 0){
	printf("Der Wert %d ist durch 3 restlos teilbar\n", Wert);
	}
	else{
		printf("Der Wert %d ist nicht durch 3 restlos teilbar\n", Wert);
		printf("%d mal %d = %d", Wert, 2, Wert * 2);
	}

	return EXIT_SUCCESS;
}
