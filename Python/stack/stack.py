#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Stack data structure (DS) module.

Python list DS can be used as a stack.

See Also
--------
https://docs.python.org/3/tutorial/datastructures.html
"""


__author__ = "Stanislav D. Kudriavtsev"


from typing import Any, List, Sequence


# Complexity: worst case

# Operation : array-based : list-based

# __bool__ : O(1) : O(1)
# __eq__   : O(n) : O(n)
# __len__  : O(1) : O(n) or O(1)
# is_empty : see __bool__
# peak     : O(1) : O(n) or O(1)
# pop      : O(1) : O(1)
# push     : O(1) : O(n) or O(1)


class ListStack:
    """Stack list-based implementation."""

    __slots__ = ["_stack"]

    def __init__(self, iterable: Sequence = None):
        if iterable is None:
            iterable = []
        self._stack: List = list(iter(iterable))

    def __bool__(self):
        return bool(self.stack)

    def __eq__(self, other):
        return self.stack == other

    def __len__(self):
        return len(self.stack)

    def __repr__(self):
        return repr(self.stack)

    def __reversed__(self):
        return ListStack(reversed(self.stack))

    def __str__(self):
        return str(self.stack)

    @property
    def is_empty(self) -> bool:
        """
        Check if stack is empty.

        Returns
        -------
        bool

        """
        return not bool(self)

    @property
    def stack(self) -> List:
        """
        Return the stack as a list.

        Returns
        -------
        List

        """
        return self._stack

    @property
    def peak(self) -> Any:
        """
        Return the last element of stack.

        Returns
        -------
        Any:
            the last element or None if stack is empty.

        """
        if self.stack:  # __bool__
            return self.stack[-1]  # len(self) - 1
        return None

    def pop(self):
        """
        Delete and return the first element from stack.

        Raises
        ------
        IndexError
            if pop() from empty stack

        Returns
        -------
        Any
            the last element from a non-empty stack.

        """
        self._stack.pop()

    def push(self, element: Any):
        """
        Add element to the back of stack.

        Parameters
        ----------
        element : Any

        Returns
        -------
        None.

        """
        self._stack.append(element)
