
#include <stdio.h> 
#include <stdlib.h>
#include <math.h>


int f(int x){
    int y = 0;
    y = 0.5*(pow(x,4))-2*(pow(x,2)) + x - 1; 
    return y;
}

int funktion(int start, int stop, int step, int mid, float erg, int steb, float ergg){
    

    if  (start > stop){
        return 0;
    }
    else{
        steb = step/2;
        mid = (start+steb);
        erg = f(mid);
        ergg = erg*start;
        printf("%f\n", ergg);
        start = start + step;
 
        funktion(start,stop,step,mid,erg,steb,ergg);

            if (ergg < 0){
                ergg = ergg*-1;
            }

    }
    return ergg;
}


int main(void) {

int start = -2;
int stop = 2;
int step = 1;
int steb = 0;
float ergg = 0;


int mid = 0;
float erg = 0;

funktion(start,stop,step,mid,erg, steb, ergg);

	return EXIT_SUCCESS;
}
