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
from typing import Any, Iterable, List, Optional


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
        if iterable is not None:
            for element in iterable:
                stack.push(element)
        return stack

    def __init__(self, maxlen: Optional[int] = None):
        # import pdb; pdb.set_trace()
        if maxlen:
            if not isinstance(maxlen, int):
                raise TypeError("maxlen is not integer")
            if maxlen < 0:
                raise ValueError("maxlen is negative")
        self._maxlen: Optional[int] = maxlen
        self._stack: List = []

    def __bool__(self):
        return bool(self.stack)

    def __eq__(self, other):
        return self.stack == other

    def __len__(self):
        return len(self.stack)

    def __lt__(self, other):
        return self.stack < other

    def __repr__(self):
        return repr(self.stack)

    def __str__(self):
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
        Return stack as a list.

        Returns
        -------
        List

        """
        return self._stack

    def empty(self) -> bool:
        """
        Check if stack is empty.

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
            the last element or None if stack is empty.

        """
        if self.stack:
            return self.stack[-1]
        return None

    def pop(self):
        """
        Delete and return the first element from stack.

        Raises
        ------
        StackError
            if self.pop() from an empty stack.

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
        Add element to the back of stack.

        Parameters
        ----------
        element : Any

        Raises
        ------
        StackError
            stack overflow if maxlen is defined and exceeded.

        """
        if self.maxlen and len(self) >= self.maxlen:
            raise StackError("stack overflow")
        self._stack.append(element)


class StackError(Exception):
    """Stack Exception class."""
