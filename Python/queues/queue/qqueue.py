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
from typing import Any, List, Sequence, Optional


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
    def from_iterable(cls, iterable: Sequence = None, maxlen: Optional[int] = None):
        """
        Create priority queue from a sequence with possibly defined maximum size.

        Parameters
        ----------
        cls : Queue.
        iterable : Sequence, optional
            to create queue. The default is None.
        maxlen : int
            the maximum size of a queue.

        Raises
        ------
        QueueError
            queue overflow if maxlen is defined and exceeded.

        Returns
        -------
        queue : Queue.

        """
        if maxlen is not None:
            cls.check_maxlen(maxlen)
        queue = cls(maxlen=maxlen)
        if iterable is not None:
            for element in iterable:
                queue.enqueue(element)
        return queue

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

    def __init__(self, maxlen: Optional[int] = None):
        # import pdb; pdb.set_trace()
        if maxlen is not None:
            self.check_maxlen(maxlen)
        self._maxlen: int = maxlen
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
            raise QueueError("dequeue from empty queue") from inderr

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


class QueueError(Exception):
    """Queue Exception class."""
