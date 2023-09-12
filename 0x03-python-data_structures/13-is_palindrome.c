#include "lists.h"

/**
 * revse_listint - func to reverse a linked list
 * @head: the pointer
 *
 * Return: to return
 */
void revse_listint(listint_t **head)
{
  listint_t *prev = NULL;
  listint_t *current = *head;
  listint_t *next = NULL;

  while (current)
    {
      next = current->next;
      current->next = prev;
      prev = current;
      current = next;
    }

  *head = prev;
}

/**
 * is_palindrome - func to check if a linked list is a palindrome
 * @head: the pointer
 *
 * Return: 1 if it is Palindrome, 0 if not
 */
int is_palindrome(listint_t **head)
{
  listint_t *slw = *head, *fst = *head, *tem = *head, *dp = NULL;

  if (*head == NULL || (*head)->next == NULL)
    return (1);

  while (1)
    {
      fst = fst->next->next;
      if (!fst)
	{
	  dp = slw->next;
	  break;
	}
      if (!fst->next)
	{
	  dp = slw->next->next;
	  break;
	}
      slw = slw->next;
    }

  revse_listint(&dp);

  while (dp && tem)
    {
      if (tem->n == dp->n)
	{
	  dp = dp->next;
	  tem = tem->next;
	}
      else
	return (0);
    }

  if (!dp)
    return (1);

  return (0);
}

