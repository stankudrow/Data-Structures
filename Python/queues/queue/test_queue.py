#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Queue test module."""


__author__ = "Stanislav D. Kudriavtsev"


from pytest import fixture, mark, param, raises

from qqueue import Queue, QueueError


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
    with raises(QueueError):
        queue.dequeue()


def test_bool():
    """bool(queue)."""
    queue = Queue()
    assert not bool(queue)
    queue.enqueue(12)
    assert bool(queue)


def test_is_empty():
    """test if queue is empty."""
    queue = Queue()
    assert queue.empty()
    queue.enqueue(12)
    assert not queue.empty()


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
    assert queue.first() is None
    queue.enqueue(1)
    assert queue.first() == 1
    queue.enqueue(2)
    assert queue.first() == 1


def test_representations():
    """repr(queue) and str(queue)."""
    elem = 123
    queue = Queue()
    queue.enqueue(123)
    lst = [elem]
    assert repr(queue) == repr(lst)
    assert str(queue) == str(lst)


@mark.parametrize(
    "data, maxlen", [(data, None),
                     (data, 0),
                     (data, 10),
                     param(4, 2, marks=mark.xfail)],
    indirect=["data"]
)
def test_from_iterable(data, maxlen):
    """Queue.from_iterable(...)."""
    queue = Queue(maxlen)
    for item in data:
        queue.enqueue(item)
    assert queue == Queue.from_iterable(data, maxlen)


def test_maxlen(data):
    """Queue(..., maxlen=...))."""
    maxlen = 10
    queue = Queue.from_iterable(data, maxlen=maxlen)
    while len(queue) < maxlen:
        queue.enqueue(-1)
    with raises(QueueError):
        queue.enqueue(0)
    with raises(QueueError):
        Queue.from_iterable(data, maxlen=2)
    with raises(TypeError):
        Queue.from_iterable(data, maxlen=2.5)
    with raises(ValueError):
        Queue.from_iterable(data, maxlen=-5)


def test_less_than_operation(data):
    """self < other"""
    queue1 = Queue()
    queue2 = Queue.from_iterable(data)
    assert queue1 < queue2
    assert queue2 >= queue1
