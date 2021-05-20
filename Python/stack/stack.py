#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Stack data structure (DS) module.

This module contains only (linked) list implementation.
In fact, the Python list DS can be perfectly used as stack.

The array-based implementation is possible, but not implemented here.
"""


__author__ = "Stanislav D. Kudriavtsev"


from typing import Any, List


# Complexity: worst case

# Operation : array-based : list-based

# __bool__ : O(1) : O(1)
# __len__  : O(1) : O(n), with counter O(1)
# is_empty : see __bool__
# peak     : O(1) : O(n), with counter O(1)
# pop      : O(1) : O(1)
# push     : O(1) : O(1)


class ListStack:
    """Stack data structure list-based implementation."""

    __slots__ = ["_stack"]

    def __init__(self):
        self._stack: List = []

    def __bool__(self):
        return bool(self.stack)

    def __eq__(self, other):
        return self.stack == other

    def __len__(self):
        return len(self.stack)

    def __repr__(self):
        return repr(self.stack)

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
        Return the stack as list.

        Returns
        -------
        List

        """
        return self._stack

    @property
    def peak(self) -> Any:
        """
        Return the last element of the stack.

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
        Delete the last element from the stack and return it.

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

    def push(self, data):
        """Push data into the stack."""
        self._stack.append(data)
