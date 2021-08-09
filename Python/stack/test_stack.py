#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""The Stack test module."""


__author__ = "Stanislav D. Kudriavtsev"


from typing import List

from pytest import fixture, mark, param, raises

from stack import Stack, StackError


# pylint: disable=arguments-out-of-order
# pylint: disable=redefined-outer-name


@fixture(autouse=True, scope='module')
def data() -> List:
    """Data fixture."""
    return [-4, 2, 0.5, None, "hey", [10], {"k": 1}]


@mark.parametrize(
    "maxlen",
    [None, 0, 2,
     param(-1, marks=mark.xfail(reason="negative")),
     param(1., marks=mark.xfail(reason="non-integer")),
     param(-1., marks=mark.xfail(reason="negative non-integer"))]
)
def test_init(maxlen):
    """Stack initialisation."""
    Stack(maxlen)


@mark.parametrize(
    "maxlen",
    [None, 0, 1, 2, 10,
     param(-1, marks=mark.xfail(reason="negative")),
     param(1., marks=mark.xfail(reason="non-integer")),
     param(-1., marks=mark.xfail(reason="negative non-integer"))]
)
def test_from_iterable(data, maxlen):
    """self.from_iterable(...)."""
    assert data[:maxlen] == Stack.from_iterable(data, maxlen)


def test_equality(data):
    """Test the equality operator."""
    stack = Stack.from_iterable(data)
    assert stack == data
    assert stack != data.append(-1)


def test_push(data):
    """self.push()."""
    stack = Stack(len(data))
    for item in data:
        stack.push(item)
    assert stack == data
    with raises(StackError):
        stack.push(1)


def test_pop(data):
    """self.push()."""
    stack = Stack.from_iterable(data)
    for _ in data:
        stack.pop()
    assert stack == []
    with raises(StackError):
        stack.pop()


def test_bool():
    """bool(self)."""
    stack = Stack()
    assert not bool(stack)
    stack.push(12)
    assert bool(stack)


def test_is_empty():
    """Test emptiness."""
    stack = Stack()
    assert stack.empty()
    stack.push(12)
    assert not stack.empty()


@mark.parametrize("data", [[], [1], [1, 2]])
def test_len(data):
    """len(self)."""
    assert len(Stack().from_iterable(data)) == len(data)


@mark.parametrize("seq", [param([], marks=mark.xfail(reason="empty")),
                          [1], [1, 2]])
def test_peak(seq):
    """self.peak()."""
    stack = Stack().from_iterable(seq)
    assert stack.peak() == stack[-1] == seq[-1]


def test_representations(data):
    """repr(self) and str(self)."""
    stack = Stack().from_iterable(data)
    assert repr(stack) == repr(data)
    assert str(stack) == str(data)


def test_less_than_operation(data):
    """self < other"""
    stack1 = Stack()
    stack2 = Stack.from_iterable(data)
    assert stack1 < stack2
    assert stack2 >= stack1


def test_iterableness(data):
    """Test iterableness."""
    istack = iter(Stack.from_iterable(data))
    for item in data:
        assert item == next(istack)
    with raises(StopIteration):
        next(istack)
