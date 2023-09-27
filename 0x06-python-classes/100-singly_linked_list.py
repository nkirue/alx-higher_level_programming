#!/usr/bin/python3
"""This defines classes for a singly-linked list."""


class Node:
    """This represents a node in a singly-linked list."""

    def __init__(self, data, next_node=None):
        """this initialize a new Node.
            the data represents the data of the new Node.
            the next_node of the new Node.
        """
        self.data = data
        self.next_node = next_node

    @property
    def data(self):
        """This is the Get/set the data of the Node."""
        return (self.__data)

    @data.setter
    def data(self, value):
        if not isinstance(value, int):
            raise TypeError("data must be an integer")
        self.__data = value

    @property
    def next_node(self):
        """This is the Get/set the next_node of the Node."""
        return (self.__next_node)

    @next_node.setter
    def next_node(self, value):
        if not isinstance(value, Node) and value is not None:
            raise TypeError("next_node must be a Node object")
        self.__next_node = value


class SinglyLinkedList:
    """singly-linked list class."""

    def __init__(self):
        """Initalizes SinglyLinkedList."""
        self.__head = None

    def sorted_insert(self, value):
        """This insert a new Node  """
        newnd = Node(value)
        if self.__head is None:
            newnd.next_node = None
            self.__head = newnd
        elif self.__head.data > value:
            newnd.next_node = self.__head
            self.__head = newnd
        else:
            temp = self.__head
            while (temp.next_node is not None and
                    temp.next_node.data < value):
                temp = temp.next_node
            newnd.next_node = temp.next_node
            temp.next_node = newnd

    def __str__(self):
        """This defines the print() """
        values = []
        temp = self.__head
        while temp is not None:
            values.append(str(temp.data))
            temp = temp.next_node
        return ('\n'.join(values))
