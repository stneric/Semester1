#include <stdio.h>
#include <stdlib.h>

int main(void){


int array[3][5] = {{1,2,3,4,0}, {5,6,7,8,0}, {26,40,58,80}};

int sum = 0;
int sum2 = 0;

for(int i = 0; i<5; i++){
    sum = sum + array[0][i];
    sum2 = sum2 + array[1][i];


    }
    array[0][4] = sum;
    array[1][4] = sum2;


printf("Erste Summe: %d\n", sum);
printf("Zweite Summe: %d\n", sum2);

for (int i = 0; i<5; i++){
    printf("%d ", array[0][i]);
}

printf("\n");

for(int i = 0; i<5; i++){
    printf("%d ", array[1][i]);
}

printf("\n");

int sum3 = 0;

for(int i = 0; i<5; i++){
    sum3 = sum3 + array[2][i];
}

array[2][4] = sum3;

if (sum3 == 776){
    printf("die Summe ist 776\n");
}
else if (sum3 != 776){
    printf("Die richtige Summe ist %d\n", sum3);
}

for(int i = 0; i<5; i++){
    printf("%d ", array[2][i]);
}


return EXIT_SUCCESS;
}