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
from typing import Any, Iterable, Iterator, List, Optional, Union


# Complexity: worst case

# Operation :

# __bool__      : O(1)
# __eq__        : O(n)
# __getitem__   : O(n)
# __len__       : O(n) or O(1)
# __lt__        : O(n)
# dequeue       : O(n) or O(1)
# empty         : __bool__
# enqueue       : O(n) or O(1)
# first         : O(1)
# from_sequence : O(n)


# __iter__ and __next__ make the Queue class iterable + __sorted__ is enabled.
# __getitem__ and __len__ make the Queue class subscriptable


@total_ordering
class Queue:
    """Queue list-based implementation."""

    __slots__ = ("_queue", "_maxlen")

    @classmethod
    def from_iterable(
        cls, iterable: Optional[Iterable] = None, maxlen: Optional[int] = None
    ) -> "Queue":
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
        if iterable:
            if maxlen is not None:
                for elem, _ in zip(iterable, range(maxlen)):
                    queue.enqueue(elem)
            else:
                for elem in iterable:
                    queue.enqueue(elem)
        return queue

    def __init__(self, maxlen: Optional[int] = None):
        self._queue: List = []
        if maxlen:
            if not isinstance(maxlen, int):
                raise TypeError("maxlen is not integer")
            if maxlen < 0:
                raise ValueError("maxlen is negative")
        self._maxlen: Optional[int] = maxlen

    def __bool__(self) -> bool:
        """
        Return True if the queue is non-empty.

        Returns
        -------
        bool

        """
        return bool(self.queue)

    def __eq__(self, other):
        """
        Return True if the queue is equal to the other object.

        Parameters
        ----------
        other

        Returns
        -------
        bool

        """
        return self.queue == other

    def __getitem__(self, index: Union[int, slice]) -> Any:
        """
        Return the value(s) at the index.

        Parameters
        ----------
        index : Union[int, slice]
            either an int value or a slice object.

        Raises
        ------
        IndexError
            if the index is out of range.

        Returns
        -------
        Any
            the element of the queue or the slice as a list.

        """
        try:
            return self.queue[index]
        except IndexError as inderr:
            raise IndexError("queue index out of range") from inderr

    def __iter__(self) -> Iterator:
        """
        Return the iterator of the queue.

        Returns
        -------
        Iterator

        """
        for item in self.queue:
            yield item

    def __len__(self) -> int:
        """
        Return the length/size of the queue.

        Returns
        -------
        int

        """
        return len(self.queue)

    def __lt__(self, other) -> bool:
        """
        Return True if the queue is less than the other object.

        Parameters
        ----------
        other

        Returns
        -------
        bool

        """
        return self.queue < other

    def __repr__(self) -> str:
        """
        Return the queue as a representation.

        Returns
        -------
        str

        """
        return repr(self.queue)

    def __str__(self) -> str:
        """
        Return the queue as a string.

        Returns
        -------
        str

        """
        return str(self.queue)

    @property
    def maxlen(self) -> Optional[int]:
        """
        Return the maximum length of the queue.

        Returns
        -------
        Optional[int]

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

    def dequeue(self) -> Any:
        """
        Pop the first element from the queue.

        Raises
        ------
        QueueError
            dequeuing from an empty queue.

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
        Return True if the queue is empty.

        Returns
        -------
        bool

        """
        return not bool(self)

    def enqueue(self, element: Any):
        """
        Add the element to the rear of the queue.

        Parameters
        ----------
        element : Any

        Raises
        ------
        QueueError
            enqueuing if maxlen is defined and exceeded.

        """
        if (self.maxlen is not None) and (len(self) >= self.maxlen):
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
        return self[0]


class QueueError(Exception):
    """Queue Exception class."""
