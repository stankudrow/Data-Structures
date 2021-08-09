#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Stack data structure (DS) module.

Python list DS can be used as a stack.

See Also
--------
https://docs.python.org/3/tutorial/datastructures.html#using-lists-as-stacks
"""


__author__ = "Stanislav D. Kudriavtsev"


from functools import total_ordering
from typing import Any, Iterable, Iterator, List, Optional, Union


# Complexity: worst case

# Operation :

# __bool__  : O(1)
# __eq__    : O(n)
# __len__   : O(n) or O(1)
# __lt__    : O(n)
# empty     : __bool__
# reverse   : O(n)
# peak      : O(n) or O(1)
# pop       : O(n) or O(1)
# push      : O(n) or O(1)


# A simpler "redefinition" is `class Stack(list)`.
# Python list can be used as a stack, but the stack is not the list.
# Here a stack is created "from zero".


@total_ordering
class Stack:
    """Stack list-based implementation."""

    __slots__ = ("_stack", "_maxlen")

    @classmethod
    def from_iterable(cls,
                      iterable: Optional[Iterable] = None,
                      maxlen: Optional[int] = None) -> 'Stack':
        """
        Create stack from an iterable object.

        Parameters
        ----------
        cls : Stack
        iterable : Optional[Iterable], optional
        maxlen : Optional[int], optional

        Returns
        -------
        Stack

        """
        stack = cls(maxlen=maxlen)
        if iterable:
            if maxlen is not None:
                for elem, _ in zip(iterable, range(maxlen)):
                    stack.push(elem)
            else:
                for elem in iterable:
                    stack.push(elem)
        return stack

    def __init__(self, maxlen: Optional[int] = None):
        self._stack: List = []
        if maxlen:
            if not isinstance(maxlen, int):
                raise TypeError("maxlen is not integer")
            if maxlen < 0:
                raise ValueError("maxlen is negative")
        self._maxlen: Optional[int] = maxlen

    def __bool__(self) -> bool:
        """
        Return True if the stack is non-empty.

        Returns
        -------
        bool

        """
        return bool(self.stack)

    def __eq__(self, other):
        """
        Return True if the stack is equal to the other object.

        Parameters
        ----------
        other

        Returns
        -------
        bool

        """
        return self.stack == other

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
            return self.stack[index]
        except IndexError as inderr:
            raise IndexError("stack index out of range") from inderr

    def __iter__(self) -> Iterator:
        """
        Return the iterator of the stack.

        Returns
        -------
        Iterator

        """
        for item in self.stack:
            yield item

    def __len__(self) -> int:
        """
        Return the length/size of the stack.

        Returns
        -------
        int

        """
        return len(self.stack)

    def __lt__(self, other) -> bool:
        """
        Return True if the stack is less than the other object.

        Parameters
        ----------
        other

        Returns
        -------
        bool

        """
        return self.stack < other

    def __repr__(self) -> str:
        """
        Return the stack as a representation.

        Returns
        -------
        str

        """
        return repr(self.stack)

    def __str__(self) -> str:
        """
        Return the stack as a string.

        Returns
        -------
        str

        """
        return str(self.stack)

    @property
    def maxlen(self) -> Optional[int]:
        """
        Return the maximum length of stack.

        Returns
        -------
        Optional[int]

        """
        return self._maxlen

    @property
    def stack(self) -> List:
        """
        Return the stack as a list.

        Returns
        -------
        List

        """
        return self._stack

    def empty(self) -> bool:
        """
        Check if the stack is empty.

        Returns
        -------
        bool

        """
        return not bool(self)

    def peak(self) -> Any:
        """
        Return the last element of stack.

        Returns
        -------
        Any:
            the last element or None if the stack is empty.

        """
        if self.stack:
            return self.stack[-1]
        return None

    def pop(self):
        """
        Delete and return the first element from the stack.

        Raises
        ------
        StackError
            popping from an empty stack.

        Returns
        -------
        Any
            the last element from a non-empty stack.

        """
        if self.empty():
            raise StackError("pop from an empty stack")
        return self._stack.pop()

    def push(self, element: Any):
        """
        Add element to the rear of the stack.

        Parameters
        ----------
        element : Any

        Raises
        ------
        StackError
            stack overflow if the maxlen is defined and exceeded.

        """
        if self.maxlen and len(self) >= self.maxlen:
            raise StackError("stack overflow")
        self._stack.append(element)


class StackError(Exception):
    """Stack Exception class."""
