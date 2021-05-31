#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Stack test module."""


__author__ = "Stanislav D. Kudriavtsev"


from pytest import fixture, mark, param, raises

from stack import Stack, StackError


# pylint: disable=arguments-out-of-order
# pylint: disable=redefined-outer-name


@fixture
def data():
    """List of data items pytest fixture."""
    return [-4, 0.5, None, "hey", [10]]


def test_init():
    """Stack initialisation."""
    stk = Stack()
    assert stk == []  # __eq__ is tested implicitly


def test_push(data):
    """stack.push(item)."""
    stk = Stack()
    lst = []
    for item in data:
        stk.push(item)
        lst.append(item)
    assert stk == lst


def test_pop():
    """stack.pop()."""
    stk = Stack()
    stk.push(12)
    stk.pop()
    assert stk == []
    with raises(StackError):
        stk.pop()


def test_bool_and_is_empty():
    """bool(stack) and stack.is_empty."""
    stk = Stack()
    stk.push(12)
    assert bool(stk) and not stk.empty
    stk.pop()
    assert not bool(stk) and stk.empty


def test_len():
    """len(stack)."""
    stk = Stack()
    assert len(stk) == 0
    stk.push(12)
    assert len(stk) == 1
    stk.push(24)
    assert len(stk) == 2


def test_peak():
    """stack.peak."""
    stk = Stack()
    assert stk.peak is None
    stk.push(1)
    assert stk.peak == 1
    stk.push(2)
    assert stk.peak == 2


def test_representations():
    """repr(stack) and str(stack)."""
    elem = 123
    stk = Stack()
    stk.push(123)
    lst = [elem]
    assert repr(stk) == repr(lst)
    assert str(stk) == str(lst)


@mark.parametrize(
    "data, maxlen", [(data, None), param(data, 0, marks=mark.xfail)], indirect=["data"]
)
def test_from_iterable(data, maxlen):
    """Stack.from_iterable(...)."""
    stack = Stack(maxlen)
    for item in data:
        stack.push(item)
    assert stack == Stack.from_iterable(data, maxlen)


def test_maxlen(data):
    """Stack(..., maxlen=...))."""
    maxlen = 10
    stk = Stack.from_iterable(data, maxlen=maxlen)
    while len(stk) < maxlen:
        stk.push(-1)
    with raises(StackError):
        stk.push(0)
    with raises(StackError):
        Stack.from_iterable(data, maxlen=2)
    with raises(TypeError):
        Stack.from_iterable(data, maxlen=2.5)
    with raises(ValueError):
        Stack.from_iterable(data, maxlen=-5)


def test_reverse(data):
    """stack.reverse() (in-place)."""
    stk = Stack.from_iterable(data)
    stk.reverse()
    assert Stack.from_iterable(reversed(data)) == stk
