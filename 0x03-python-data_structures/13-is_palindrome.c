#include "lists.h"
#include <stdlib.h>
#include <stdio.h>
#include <stddef.h>

/**
 * is_palindrome- Checks wheather a singly linked list is a palindrome.
 * @head: the head pointer
 * Return: 0 if it is not a palindrome or 1 if it is a palindrome.
 */
int is_palindrome(listint_t **head)
{
	listint_t *node;
	int value[9999], i = 0, c = 0;

	if ((!*head) || (!head))
	{
		return (1);
	}
	node = *head;
	if (!node->next)
	{
		return (1);
	}
	while (node)
	{
		values[i] = node->n;
		node = node->next;
		i++;
	}
	i--;
	while (i >= 0 && c <= i)
	{
		if (values[i] != values[c])
		{
			return (0);
		}
		i--;
		c++;
	}
	return (1);
}
