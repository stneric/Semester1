#include <stdlib.h>
#include <stdio.h>

//Aufgabe Eingaben
//Der Code funktioniert aus irgendwelchen Gründen bei mir nicht und ich kann keine Fehler suchen.

int main(void){

    char geschlecht[1];
    int matrikelnummer[7];
    char name[10];
    char studiengang[5];


        printf("Geschlecht (Bitte nur m/w/d eingeben) :'');
        scanf('%c', &geschlecht);

        printf('Martrikelnummer (6 Ziffern) :');
        scanf('%i', &matrikelnummer);

        printf('Name:');
        scanf('%s', &name);}

        printf('Studiengang (mki/meti/wi) :');
        scanf('%s', &studiengang);


    printf('Dein Name ist:"', '%s', name);
    printf('Deine Matrikelnummer ist:', '%i', matrikelnummer);
    printf('Dein Geschlecht ist:', '%c', geschlecht);

    return EXIT_SUCCESS;

    }

//AUFGABE Hello World formatted.

int main(void){

printf("Hello World!\n");
printf("    Hello World!\n");
printf("        Hello World!\n");
printf("            Hello World!\n");


    return EXIT_SUCCESS;

    }

// SPIEL

#include <stdio.h>
#include <stdlib.h>


int main(void){

  int age1;
  int age2;

  char name1[20];
  char name2[20];

printf("Wie alt ist Spieler 1?");
scanf("%d", &age1);

printf("Wie alt ist Spieler 2?");
scanf("%d", &age2);

if ((age1 - age2) < 10 && (age1 - age2) > -10){
printf("Nur ein Testspiel ist möglich. \n");
}
else {
printf("Das Spiel kann beginnen\n");
}


if ((age1) < 16 || (age2) < 16){
  printf("Es ist keine Teilnahme möglich\n");
}
else {
  printf("Das Spiel kann beginnen\n");
}



  return EXIT_SUCCESS;

}
