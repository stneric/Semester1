/*
 ============================================================================
 Name        : Probeprogrammiertest2.c
 Author      : 
 Version     :
 Copyright   : Your copyright notice
 Description : Hello World in C, Ansi-style
 ============================================================================
 */

#include <stdio.h>
#include <stdlib.h>

int main(void) {

	//A1

	int feld[] = {10,11,12,13,14,15,16,17,18,19};

	printf("%d\n", feld[0]);
	printf("%d\n", feld[9]);
	printf("%d\n", feld[3]);


	for (int i = 0; i<10; i++	){
		if ( i==4){
			feld[i] = 20;
		}
	}

	int var1 = feld[1];
	int var2 = feld[7];

	for (int i = 0; i<10; i++){
		if ( i==1){
			feld[i] = var2;
		}
		else if(i == 7){
			feld[i] = var1;
		}
	}

	for(int i = 0; i<10; i++){
		printf("%d, ", feld[i]);
	}

	return EXIT_SUCCESS;
}
