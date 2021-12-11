//
//
//#include <stdio.h>
//#include <stdlib.h>
//#include <math.h>
//
////Aufgabe 1
//
//int simpexp(){
//
//	int b = 10;
//	int x = 3;
//	int y = 0;
//	int z = 0;
//	int p = 0;
//
//	//  a)
//
//	if(x == 1){
//		b = pow(b,x);
//	}
//
//
//	//  b)
//
//	else if(x%2 == 0){
//		z = x-1;
//		b = b * pow(b,z);
//	}
//
//
//	//  c) Nachfragen
//
//		else if(x%2 > 0){
//			y = (x/2)*2;
//			p = pow(b,y);
//			b = p*p;
//		}
//
//	printf("%d", b);
//}
//
//
//
//int main(void) {
//
////	a. Wenn der Exponent x = 1 ist, dann gilt: b^x = b
//
////	b. Wenn der Exponent x gerade ist, dann gilt: b^x = b * b^(x-1)
//
////	c. Wenn der Exponent x ungerade ist, dann gilt: b^x = b^x/2 * b^x/2
//
//
//
//	simpexp();
//
//	return EXIT_SUCCESS;
//}




#include <stdio.h>
#include <stdlib.h>
#include <math.h>

float func(x){

    float y = (pow(x,3)-(2*pow(x,2))+x-3);
    printf("%f", y);
    return y;

}

float integrate(float start, float stop, int counter){

    float summe = 0;
    float summee = 0;

    if (start>stop){
        return 0;
    }
    else{
        float y = func(start);
        float erg = y*start;

        if (erg<0){
            erg = erg*(-1);
            printf("Fläche für %.1f = %.1f\n", start, erg);
            summe = summe + erg;
            integrate(start+1, stop, counter);
        }
        else{
            printf("Fläche für %.1f = %.1f\n", start, erg);
            summee = summee + erg;
            integrate(start+1, stop, counter);
        }
    }
        printf("Die gesamte Fläche ist = %.1f\n", summe+summee);

}

int main(void){

    integrate(1,5,0);

}






