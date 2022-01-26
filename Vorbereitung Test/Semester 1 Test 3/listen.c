
#include <stdio.h>
#include <stdlib.h>


//new type
typedef struct listElement
{
	int id;
	//pointers to next and prev element
	struct listElement* next;
	struct listElement* prev;
} elem;


struct list
{
	//pointer to element
	elem *head;
	elem *tail;
};

void printList(struct list* l)
{
	if(l->head == NULL)
	{
		printf("list is empty");
		return;
	}
	//temporary list element
	elem* temp = l->head;
	while(temp != NULL)
	{
		printf("%d", temp->id);
		temp = temp->next;
	}
}


int pushElem(struct list* l, int id)
{
	//alloc space with the size of elem
	elem* current = malloc(sizeof(elem));
	//if there is no space to allocate
	if(current == NULL)
	{
		printf("no space");
		return -1;
	}

	//init current
	current->id = id;

	if(l->head == NULL)
	{
		l->head = current;
		l->tail = current;
	}
	else
	{
		current->next = l->head;
		l->head->prev = current; //adress from current to prev
		l->tail = current;
	}
	return 0;
}






int main(void) {
    struct list* l = malloc(sizeof(struct list));
	struct list* nums = malloc(sizeof(struct list));
	nums.head = NULL;
	nums.tail = NULL;

	pushElem(&nums, 1);
	pushElem(&nums, 2);
	pushElem(&nums, 3);

	printList(&nums);
	printf("nig");

	return EXIT_SUCCESS;
}

