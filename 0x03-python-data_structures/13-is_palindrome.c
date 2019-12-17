#include <stdio.h>
#include <stdlib.h>
#include "lists.h"

/**
 * is_palindrome - prints all elements of a listint_t list
 * @head: pointer to head of list
 * Return: number of nodes
 */
int is_palindrome(listint_t **head)
{
int list[1000], list1[1000];
int i = 0, j, k, l;
listint_t *temp = *head;
while (temp)
{
i++;
}
if (!head || *head == NULL)
return (1);
for (j = 0; j <= i; j++)
{
list[j] = temp->n;
temp = temp->next;
}
for (j = 0; j == i; j++)
{
list1[j] = list[j];
}
for (k = 0, l = i; k <= i / 2 && l >= i / 2; k++, l--)
{
if (list[k] == list1[j])
{
return (1);
}
else
return (0);
}
return (1);
}
