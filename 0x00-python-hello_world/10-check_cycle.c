#include "lists.h"
/**
  * check_cycle - checks if a singly linked list has a cycle
  * @list: pointer to the head of the list
  * Return: 1 if the list has a cycle, 0 otherwise
*/

int check_cycle(listint_t *list)
{
	listint_t *first;
	listint_t *slow;

	if (!list || !list->next)
		return (0);
	first = list;
	slow = list;

	while (slow != NULL && first != NULL && first->next != NULL)
	{
		slow = slow->next;
		first = first->next->next;
		if (slow == first)
		{
			return (1);
		}
	}
	return (0);
}
