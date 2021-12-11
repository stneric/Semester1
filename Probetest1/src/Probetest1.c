/*
 ============================================================================
 Name        : Probetest1.c
 Author      : 
 Version     :
 Copyright   : Your copyright notice
 Description : Hello World in C, Ansi-style
 ============================================================================
 */

#include <stdio.h>
#include <stdlib.h>

int main(void) {


//	int array[3][5] = {{1,2,3,4,0},{5,6,7,8,0},{26,40,58,80,0}};
//
//	int sum = 0;
//	int sum2 = 0;
//
//	for (int i = 0; i<5; i++){
//
//		sum = sum + array[0][i];
//		sum2 = sum2 + array[1][i];
//	}
//
//	printf("Summe Zeile 1 = %d, Zeile 2 = %d\n", sum, sum2);
//
//	for (int i = 0; i < 5; i++){
//		if ( array[0][i]==0){
//			array[0][i] = sum;
//		}
//		else if (array[1][i]==0){
//			array[1][i] = sum2;
//		}
//	}
//
//	for(int i = 0; i<5; i++){
//		printf("%d ", array[0][i]);
//
//	}
//
//	printf("\n");
//
//	for(int i = 0; i<5; i++){
//		printf("%d ", array[1][i]);
//	}
//	printf("\n");
//
//
//
//
//	// Pruefen ob summe stimmt
//
//int summ = 0;
//
//	for ( int i = 0; i<5; i++){
//		summ = summ + array[2][i];
//	}
//
//	for(int i = 0; i<5; i++){
//		if(array[2][i]== 0){
//			array[2][i] = summ;
//		}
//	}
//
//	if (summ == 776){
//		printf("Die Summe ist 776\n");
//	}
//	else if(summ != 776){
//		printf("Die tatsächliche Summe ist %d\n", summ);
//	}
//
//	for(int i = 0; i<5; i++){
//		printf("%d ", array[2][i]);
//	}
//	printf("\n");


int array[3][5] = {{1,2,3,4,0},{5,6,7,8,0}};

int sum = 0;

for (int i = 0; i < 4; i++){

	sum = array[0][i] + sum;
	array[0][4] = sum;
	}

sum = 0;

for (int i = 0; i < 4; i++){

	sum = array[1][i] + sum;
	array[1][4] = sum;
	}

sum = 0;

for (int i = 0; i < 4; i++){

	sum = array[2][i] + sum;
	array[2][4] = sum;
	}


for(int j = 0; j < 3; j++){
	for (int i = 0; i < 5; i++){

		printf("%d ", array[j][i]);

		if ( i == 4 ){
			printf("\n");
		}

	}
}










	return EXIT_SUCCESS;
}
