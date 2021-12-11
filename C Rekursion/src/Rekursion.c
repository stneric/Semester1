#include <stdio.h>
#include <stdlib.h>


int iteration(int x, int y, int summe){

	for(int i = x; i<=y; i++){
	    if(x<=y){
		summe = summe + i;
		printf("\n Schritt: %d ergibt %d.\n ", i, summe);

		}

	}
	printf("\n Die Summe von ist also %d.\n ", summe);

	return 0;
}


int rekursion(int x, int y, int z, int i){
	x = i;
	if(x<=y){
		x = i+i;
		z = x + i;
		rekursion(x,y,z,i+1);
	//Manchmal kommt die richtige Zahl raus, manchmal die falsche. Ich finde den Fehler aber nicht :D
	}
	else{
		printf("Summe = %d\n", z);

	}

}


int main(void){

	int x;
	int y;
    int summe;
    int i;
    int z;


	printf("X:");
	scanf("%d", &x);

	printf("Y:");
	scanf("%d", &y);

//	iteration(x,y,summe);
	rekursion(x,y,i,z);

}
