#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Queue data structure (DS) module.

Python provides the following tools:

    * list DS can be used as a queue;

    * queue module.

See Also
--------
https://docs.python.org/3/tutorial/datastructures.html#using-lists-as-queues
https://docs.python.org/3/library/queue.html
"""


__author__ = "Stanislav D. Kudriavtsev"


from functools import total_ordering
from typing import Any, Iterable, List, Optional


# Complexity: worst case

# Operation :

# __bool__      : O(1)
# __eq__        : O(n)
# __len__       : O(n) or O(1)
# __lt__        : O(n)
# dequeue       : O(n) or O(1)
# empty         : __bool__
# enqueue       : O(n) or O(1)
# first         : O(1)
# from_iterable : O(n)
# reverse       : O(n)


@total_ordering
class Queue:
    """Queue list-based implementation."""

    __slots__ = ("_queue", "_maxlen")

    @classmethod
    def from_iterable(cls,
                      iterable: Optional[Iterable] = None,
                      maxlen: Optional[int] = None) -> 'Queue':
        """
        Create queue from an iterable object.

        Parameters
        ----------
        cls : Queue
        iterable : Optional[Iterable], optional
        maxlen : Optional[int], optional

        Returns
        -------
        Queue

        """
        queue = cls(maxlen=maxlen)
        if iterable is not None:
            for element in iterable:
                queue.enqueue(element)
        return queue

    def __init__(self, maxlen: Optional[int] = None):
        # import pdb; pdb.set_trace()
        if maxlen:
            if not isinstance(maxlen, int):
                raise TypeError("maxlen is not integer")
            if maxlen < 0:
                raise ValueError("maxlen is negative")
        self._maxlen: Optional[int] = maxlen
        self._queue: List = []

    def __bool__(self):
        return bool(self.queue)

    def __eq__(self, other):
        return self.queue == other

    def __len__(self):
        return len(self.queue)

    def __lt__(self, other):
        return self.queue < other

    def __repr__(self):
        return repr(self.queue)

    def __str__(self):
        return str(self.queue)

    @property
    def maxlen(self) -> Optional[int]:
        """
        Return the maximum length of stack.

        Returns
        -------
        int

        """
        return self._maxlen

    @property
    def queue(self) -> List:
        """
        Return the queue as a list.

        Returns
        -------
        List

        """
        return self._queue

    def dequeue(self):
        """
        Delete and return the first element from queue.

        Raises
        ------
        QueueError
            if self.dequeue() from an empty queue.

        Returns
        -------
        Any
            the first element from a non-empty queue.

        """
        try:
            return self._queue.pop(0)
        except IndexError as inderr:
            raise QueueError("dequeue from an empty queue") from inderr

    def empty(self) -> bool:
        """
        Check if queue is empty.

        Returns
        -------
        bool

        """
        return not bool(self)

    def enqueue(self, element: Any):
        """
        Add element to the back of queue.

        Parameters
        ----------
        element : Any

        Raises
        ------
        QueueError
            queue overflow if maxlen is defined and exceeded.

        """
        if self.maxlen and len(self) >= self.maxlen:
            raise QueueError("queue overflow")
        self._queue.append(element)

    def first(self) -> Any:
        """
        Return the first element from queue without removing it.

        Returns
        -------
        Any:
            the first element or None if the queue is empty.

        """
        if self.queue:
            return self.queue[0]
        return None


class QueueError(Exception):
    """Queue Exception class."""
