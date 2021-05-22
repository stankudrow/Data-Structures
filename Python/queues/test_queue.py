#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Queue test module."""


__author__ = "Stanislav D. Kudriavtsev"


from pytest import fixture, raises

from qqueue import ListQueue as Queue


# pylint: disable=arguments-out-of-order
# pylint: disable=redefined-outer-name


@fixture
def data():
    """List of data items pytest fixture."""
    return [-4, 0.5, None, "hey", [10]]


def test_init():
    """Queue initialisation."""
    queue = Queue()
    assert queue == []  # __eq__ is tested implicitly


def test_enqueue(data):
    """queue.enqueue(item)."""
    queue = Queue()
    lst = []
    for item in data:
        queue.enqueue(item)
        lst.append(item)
    assert queue == lst


def test_dequeue():
    """queue.dequeue()."""
    queue = Queue()
    queue.enqueue(12)
    queue.dequeue()
    assert queue == []
    with raises(IndexError):
        queue.dequeue()


def test_bool_and_is_empty():
    """bool(queue) and queue.is_empty."""
    queue = Queue()
    queue.enqueue(12)
    assert bool(queue) and not queue.is_empty
    queue.dequeue()
    assert not bool(queue) and queue.is_empty


def test_len():
    """len(queue)."""
    queue = Queue()
    assert len(queue) == 0
    queue.enqueue(12)
    assert len(queue) == 1
    queue.enqueue(24)
    assert len(queue) == 2


def test_first():
    """queue.first."""
    queue = Queue()
    assert queue.first is None
    queue.enqueue(1)
    assert queue.first == 1
    queue.enqueue(2)
    assert queue.first == 1


def test_representations():
    """repr(queue) and str(queue)."""
    elem = 123
    queue = Queue()
    queue.enqueue(123)
    lst = [elem]
    assert repr(queue) == repr(lst)
    assert str(queue) == str(lst)


def test_reversed(data):
    """reversed(queue)."""
    queue = Queue(data)
    assert reversed(queue) == list(reversed(data))
