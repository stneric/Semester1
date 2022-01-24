#include <stdlib.h>
#include <string.h>
#include <stdio.h>

typedef struct{
    char title[20];
    char name[20];
    int pages;
    char genre[50];
    char grade;
}book;

int main(void){

    book* Batman = malloc(sizeof(book));
    if (&malloc == NULL){
        return -1;
    }
    
    else{
    strcpy(Batman->title, "Batman");
    strcpy(Batman->name, "The Dark Knight");
    Batman->pages = 342;
    strcpy(Batman->genre, "Action");
    Batman->grade = 'B';

    printf("Name: %s: %s, \n%d pages, \nGenre: %s, \nGrade: %c",Batman->title, Batman->name, Batman->pages, Batman->genre, Batman->grade);
    }
    
    printf("\nSpeicher belegt: %d",sizeof(Batman));
    free(Batman);
    printf("\nSpeicher belegt: %d",sizeof(Batman));

    return EXIT_SUCCESS;
}