#include "lists.h"

/**
 * check_cycle - check if list has a cycle
 * @head: pointer to list to be freed
 * Return: 0 if has no cycle or 1 if has cycle
 */
int check_cycle(listint_t *list)
{
listint_t *next;

if (!list || list->next == NULL)
return (0);
next = list->next;
while (next != NULL && next != list)
next = next->next;
return (next == list);
}
