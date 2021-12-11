
#include <stdio.h>
#include <stdlib.h>

// Fakultätsfunktion
int rekursion(x){

		if (x > 0){
			return x*rekursion(x-1);
		}
		else{
			return 1;
		}

	}


int iteration(int x){

	int y = 1;

	for(int i=1; i<=x;i++){

		if(x == 0){
			return 1;
		}

		else{
			y = y*i;
		}
}

	printf("%d", y);
	return y;
}




int main(void){


	//printf("%d",rekursion(5));
	iteration(5);

}
