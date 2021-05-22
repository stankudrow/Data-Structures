#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Queue data structure (DS) module.

Python provides the following tools:

    + list DS can be used as a queue;

    * deque DS from collections module;

    * queue module.

See Also
--------
https://docs.python.org/3/tutorial/datastructures.html
https://docs.python.org/3/library/queue.html
https://docs.python.org/3/library/collections.html
"""


__author__ = "Stanislav D. Kudriavtsev"


from typing import Any, List, Sequence


# Complexity: worst case

# Operation : array-based : list-based

# __bool__ : O(1) : O(1)
# __eq__   : O(n) : O(n)
# __len__  : O(1) : O(n) or O(1)
# is_empty : see __bool__
# first    : O(1) : O(n) or O(1)
# dequeue  : O(1) : O(1)
# enqueue  : O(1) : O(n) or O(1)


class ListQueue:
    """Queue list-based implementation."""

    __slots__ = ["_queue"]

    def __init__(self, iterable: Sequence = None):
        if iterable is None:
            iterable = []
        self._queue: List = list(iter(iterable))

    def __bool__(self):
        return bool(self.queue)

    def __eq__(self, other):
        return self.queue == other

    def __len__(self):
        return len(self.queue)

    def __repr__(self):
        return repr(self.queue)

    def __reversed__(self):
        return ListQueue(reversed(self.queue))

    def __str__(self):
        return str(self.queue)

    @property
    def is_empty(self) -> bool:
        """
        Check if queue is empty.

        Returns
        -------
        bool

        """
        return not bool(self)

    @property
    def queue(self) -> List:
        """
        Return the queue as a list.

        Returns
        -------
        List

        """
        return self._queue

    @property
    def first(self) -> Any:
        """
        Return the first element from queue without removing it.

        Returns
        -------
        Any:
            the first element or None if queue is empty.

        """
        if self.queue:  # __bool__
            return self.queue[0]
        return None

    def dequeue(self):
        """
        Delete and return the first element from queue.

        Raises
        ------
        IndexError
            if dequeue() from empty queue

        Returns
        -------
        Any
            the first element from a non-empty queue.

        """
        self._queue.pop(0)

    def enqueue(self, element: Any):
        """
        Add element to the back of queue.

        Parameters
        ----------
        element : Any

        Returns
        -------
        None.

        """
        self._queue.append(element)
