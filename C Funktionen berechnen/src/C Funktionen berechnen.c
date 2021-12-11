

#include <stdio.h>
#include <stdlib.h>


int ergebnis(int x, int erg){

	for(int x = 0; x<=10; x++){
		if(x<=10){
		int erg = x*x*x+24*x*x+4*x+7;

		printf("Das Ergebnis für x=%d ist %d\n", x, erg);
	}
		else{
			ergebnis(x+1,erg);
			return 0;
		}
	}
	}

//int rekursiv(b,x){
//	if(x=1);
//	return b;
//}
//		else{
//			return rekursiv(b,x-1);
//
//}




int main(void) {


	//Funktion berechnen


	int b;

	int x;
//	int y;

//	printf("Nach welchem X-Wert soll aufgelöst werden?\n");
//	scanf("%d", &x);
//	printf("Der ausgewählte x-Wert ist: %d\n", x);


int erg = x*x*x+24*x*x+4*x+7;

//	printf("Für Wert x=%d ist der Wert y=%d", x, erg);

ergebnis(x,erg);




	return EXIT_SUCCESS;
}
