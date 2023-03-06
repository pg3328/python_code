"""
cs_queue.py
author: James Heliotis, Arya Girisha Rao(ar1422@rit.edu), Pradeep Kumar Gontla(pg3328@rit.edu)
description: A linked queue (FIFO) implementation
"""
from typing import Any

from node import LinkedNode


class Queue:
    __slots__ = "front", "back", "length"
    front: LinkedNode
    back: LinkedNode
    length: int

    def __init__(self) -> None:
        """ Create a new empty queue.
        """
        self.front = None
        self.back = None
        self.length = 0

    def __str__(self) -> str:
        """ Return a string representation of the contents of
            this queue, oldest value first.
        """
        result = "Queue["
        n = self.front
        while n is not None:
            result += " " + str(n.value)
            n = n.link
        result += " ]"
        return result

    def is_empty(self) -> bool:
        return self.front is None

    def is_not_empty(self):
        return not self.is_empty()

    def enqueue(self, newValue: Any) -> None:
        newNode = LinkedNode(newValue)
        if self.front is None:
            self.front = newNode
        else:
            self.back.link = newNode
        self.back = newNode
        self.length += 1

    def dequeue(self) -> None:
        assert not self.is_empty(), "Dequeue from empty queue"
        self.front = self.front.link
        if self.front is None:
            self.back = None

    def peek(self) -> Any:
        assert not self.is_empty(), "peek on empty queue"
        return self.front.value

    def peek_back_of_queue(self) -> Any:
        assert not self.is_empty(), "peek on empty queue"
        return self.back.value

    def get_length(self) -> int:
        """
        Returns the length of the Queue
        :return: length of the Queue
        """
        return self.length

    insert = enqueue
    remove = dequeue


def test() -> None:
    s = Queue()
    print(s)
    for value in 1, 2, 3:
        s.enqueue(value)
        print(s)
    print("Dequeueing:", s.peek())
    s.dequeue()
    print(s)
    for value in 15, 16:
        s.insert(value)
        print(s)
    print("Removing:", s.peek())
    s.remove()
    print(s)
    while not s.is_empty():
        print("Dequeueing:", s.peek())
        s.dequeue()
        print(s)
    print("Trying one too many dequeues... ", end="")
    try:
        s.dequeue()
        print("Problem: it succeeded!")
    except Exception as e:
        print("Exception was '" + str(e) + "'")


if __name__ == "__main__":
    test()
