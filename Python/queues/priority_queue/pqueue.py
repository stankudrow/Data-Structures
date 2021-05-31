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


from functools import total_ordering
from typing import Any, List, Sequence, Optional, Tuple


# Complexity: worst case

# Operation :

# __bool__      : O(1)
# __eq__        : O(n)
# __iter__      : O(n)
# __len__       : O(n) or O(1)
# __lt__        : O(n)
# dequeue       : O(n) or O(1)
# empty         : __bool__
# enqueue       : O(n) or O(1)
# first         : O(1)
# from_iterable : O(n)
# reverse       : O(n)


# If two elements have the same priority,
# they are processed according to their insertion order.

@total_ordering
class PriorityQueue:
    """PriorityQueue list-based implementation."""

    __slots__ = ("_queue", "_maxlen")

    @classmethod
    def from_iterable(cls, iterable: Sequence[Tuple[Any, int]] = None, maxlen: Optional[int] = None):
        """
        Create priority queue from sequence of (element, priority) tuples.

        Parameters
        ----------
        cls : PriorityQueue.
        iterable : Sequence[Tuple[Any, int]], optional
            to create priority queue. The default is None.
        maxlen : int
            the maximum size of a priority queue.

        Returns
        -------
        pqueue : PriorityQueue.

        """
        pqueue = cls()
        if iterable is not None:
            for element, priority in iterable:
                cls.check_priority(priority)
                pqueue.enqueue(element, priority)
        return pqueue

    @staticmethod
    def check_maxlen(maxlen: int):
        """
        Check if maxlen value is valid.

        Parameters
        ----------
        maxlen : int
            the maximum size of a priority queue.

        Raises
        ------
        TypeError
            if maxlen is not of integer type.
        ValueError
            if maxlen is a negative integer.

        Returns
        -------
        None.

        """
        if not isinstance(maxlen, int):
            raise TypeError("maxlen is not integer")
        if maxlen < 0:
            raise ValueError("maxlen is negative")

    @staticmethod
    def check_priority(priority: int):
        """
        Check if priority value is valid.

        Parameters
        ----------
        priority : int
            for an element of PriorityQueue.

        Raises
        ------
        TypeError
            if priority is not of integer type.

        Returns
        -------
        None.

        """
        if not isinstance(priority, int):
            raise TypeError("priority is not integer")

    def __init__(self, maxlen: Optional[int] = None):
        # import pdb; pdb.set_trace()
        if iterable is None:
            iterable: List = []
        pqueue: List = list(iter(iterable))
        if maxlen is not None:
            self.check_maxlen(maxlen)
            if len(pqueue) > maxlen:
                raise PriorityQueueError("maxlen <= len(iterable)")
        self._maxlen = maxlen
        self._pqueue = pqueue

    def __bool__(self):
        return bool(self.queue)

    def __eq__(self, other):
        return self.queue == other

    def __iter__(self):
        return self  # by convention

    def __len__(self):
        return len(self.queue)

    def __lt__(self, other):
        return self.queue < other

    def __next__(self):
        index, size = 0, len(self)
        while index < size:
            return self.queue[index]
        raise StopIteration

    def __repr__(self):
        return repr(self.queue)

    def __str__(self):
        return str(self.queue)

    @property
    def empty(self) -> bool:
        """
        Check if queue is empty.

        Returns
        -------
        bool.

        """
        return not bool(self)

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

    @property
    def maxlen(self) -> int:
        """
        Return the maximum length of stack.

        Returns
        -------
        int.

        """
        return self._maxlen

    @property
    def queue(self) -> List:
        """
        Return the queue as a list.

        Returns
        -------
        List.

        """
        return self._queue

    def dequeue(self):
        """
        Delete and return the first element from queue.

        Raises
        ------
        IndexError
            if self.dequeue() from an empty queue.

        Returns
        -------
        Any
            the first element from a non-empty queue.

        """
        return self._queue.pop(0)

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
        if self.maxlen and len(self) >= self.maxlen:
            raise QueueError("queue overflow")
        self._queue.append(element)

    def reverse(self):
        """
        In-place reverse.

        Returns
        -------
        None.

        """
        self._queue = list(reversed(self.queue))


class PriorityQueueError(Exception):
    """PriorityQueue Exception class."""
