#include <stdio.h>
#include <stdlib.h>

typedef struct {
    int value;
    struct ListElement *next;
} ListElement;

typedef struct {
    ListElement *first;
}List;

void insert_Element(ListElement *newElement, List *list){
    ListElement *temp;
    temp = list->first;
    while (temp->next != NULL)
    {
        temp = temp->next;
    }
    temp->next = newElement;
}

void delete_Element(ListElement *delElement, List *list)
{
    ListElement *temp;
    ListElement *del;
    temp = list->first;

    if(temp == delElement)
    {
        list->first = temp->next;       // Wir setzen das naechste Element auf first 
        free(temp);     //Und geben den Speicher frei
        return;
    }
    while(temp != NULL)
    {
        if(temp->next == delElement){       //Wenn das zu loeschende Element gleich das naechste des temp ist
            del = temp->next;                       //soll das zu löschende Element mit dem naechsten von dem ueberschrieben
            temp->next = del->next;         //und dann sagen wir das Temp next = dem zu loeschendem Element next ist
            free(del);
        }
        temp = temp->next;
    }
}

void print_list(List* list){
    ListElement* temp;
    temp = list->first;
    while(temp != NULL)
    {
        printf("%d\n", temp->value);
        temp = temp->next;
    }
    printf("-------------");
}

int main()
{
    List list;

    ListElement *a;
    a = malloc(sizeof(ListElement));

    a->value = 10;
    a->next = NULL;

    list.first = a;

    ListElement *b;
    b = malloc(sizeof(ListElement));

    b->value = 9;
    b->next = NULL;

    insert_Element(b, &list);
    print_list(&list);

    delete_Element(b, &list);

    print_list(&list);

    return 0;
}