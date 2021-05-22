#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Stack test module."""


__author__ = "Stanislav D. Kudriavtsev"


from pytest import fixture, raises

from stack import ListStack as Stack


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
    with raises(IndexError):
        stk.pop()


def test_bool_and_is_empty():
    """bool(stack) and stack.is_empty."""
    stk = Stack()
    stk.push(12)
    assert bool(stk) and not stk.is_empty
    stk.pop()
    assert not bool(stk) and stk.is_empty


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


def test_reversed(data):
    """reversed(stack)."""
    stk = Stack(data)
    assert reversed(stk) == list(reversed(data))
