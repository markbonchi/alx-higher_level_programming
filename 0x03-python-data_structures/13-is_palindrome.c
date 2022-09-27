#include "lists.h"
#include <stddef.h>
#include <stdlib.h>

/**
 */

int is_palindrome(listint_t **head)
{
	int i, counter = 0, arr[24];
	listint_t *temp;

	if (*head == NULL)
		return (1);

	temp = *head;
	while (temp != NULL)
	{
		arr[counter] = temp->n;
		temp = temp->next;
		counter++;
	}

	if (counter % 2 == 0)
	{
		for(i = 0; arr[i] != arr[counter - 1]; i++, counter--)
			return (0);
		return (1);
	}
	return (0);
}
