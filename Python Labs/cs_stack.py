"""
stack.py
author: James Heliotis, Arya Girisha Rao(ar1422@rit.edu), Pradeep Kumar Gontla(pg3328@rit.edu)
description: A linked stack (LIFO) implementation
"""
from typing import Any

from node import LinkedNode


class Stack:
    __slots__ = "top", "length"
    top: LinkedNode
    length: int

    def __init__(self) -> None:
        """ Create a new empty stack."""
        self.top = None
        self.length = 0

    def __str__(self) -> str:
        """ Return a string representation of the contents of
            this stack, top value first.
        """
        result = "Stack["
        n = self.top
        while n is not None:
            result += " " + str(n.value)
            n = n.link
        result += " ]"
        return result

    def is_empty(self) -> bool:
        return self.top is None

    def is_not_empty(self) -> bool:
        return not self.is_empty()

    def push(self, newValue: Any) -> None:
        self.top = LinkedNode(newValue, self.top)
        self.length += 1

    def pop(self) -> None:
        assert not self.is_empty(), "Pop from empty stack"
        self.top = self.top.link

    def peek(self) -> Any:
        assert not self.is_empty(), "peek on empty stack"
        return self.top.value

    def get_length(self) -> int:
        """
        Returns the length of the Stack.
        :return: length of the stack.
        """
        return self.length

    insert = push
    remove = pop


def test() -> None:
    s = Stack()
    for value in 1, 2, 3:
        s.push(value)
        print(s)
    print("Popping:", s.peek())
    s.pop()
    print(s)
    for value in 15, 16:
        s.insert(value)
        print(s)
    print("Removing:", s.peek())
    s.remove()
    print(s)
    while not s.is_empty():
        print("Popping:", s.peek())
        s.pop()
        print(s)
    print("Trying one too many pops... ", end="")
    try:
        s.pop()
        print("Problem: it succeeded!")
    except Exception as e:
        print("Exception was '" + str(e) + "'")


if __name__ == "__main__":
    test()
