#include "lists.h"

/**
 * check_cycle - check if list has a cycle
 * @head: pointer to list to be freed
 * Return: 0 if has no cycle or 1 if has cycle
 */
int check_cycle(listint_t *head)
{
listint_t *next;

next = malloc(sizeof(listint_t));
next = head->next;
while (next != NULL && next != head)
next = next->next;
return (next == head);
}
