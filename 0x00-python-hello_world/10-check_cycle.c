#include "lists.h"

/**
 * check_cycle - checks cycle in a linked list
 * @list:The linked list to check
 *
 * Return: It returns 1 if the list has a cycle, 0 if it doesn't
 */
int check_cycle(listint_t *list)
{
	listint_t *slw = list;
	listint_t *fst = list;

	if (!list)
		return (0);

	while (slw && fst && fst->next)
	{
		slw = slw->next;
		fst = fst->next->next;
		if (slw == fst)
			return (1);
	}

	return (0);
}
