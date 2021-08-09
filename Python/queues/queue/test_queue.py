#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""The Queue test module."""


__author__ = "Stanislav D. Kudriavtsev"


from typing import List

from pytest import fixture, mark, param, raises

from qqueue import Queue, QueueError


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
    """Queue initialisation."""
    Queue(maxlen)


@mark.parametrize(
    "maxlen",
    [None, 0, 1, 2, 10,
     param(-1, marks=mark.xfail(reason="negative")),
     param(1., marks=mark.xfail(reason="non-integer")),
     param(-1., marks=mark.xfail(reason="negative non-integer"))]
)
def test_from_iterable(data, maxlen):
    """Queue.from_iterable(...)."""
    assert data[:maxlen] == Queue.from_iterable(data, maxlen)


def test_equality(data):
    """Test the equality operator."""
    queue = Queue.from_iterable(data)
    assert queue == data
    assert queue != data.append(-1)


# enqueue was implicitly tested in the previous tests
def test_enqueue(data):
    """queue.enqueue(item)."""
    queue = Queue()
    for item in data:
        queue.enqueue(item)
    assert queue == data


def test_dequeue(data):
    """queue.dequeue()."""
    queue = Queue.from_iterable(data)
    for _ in data:
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
    """Test if the queue is empty."""
    assert not test_bool()


@mark.parametrize("data", [[], [1], [1, 2]])
def test_len(data):
    """len(queue)."""
    assert len(Queue().from_iterable(data)) == len(data)


@mark.parametrize("seq", [param([], marks=mark.xfail), [1], [1, 2]])
def test_first(seq):
    """queue.first()."""
    queue = Queue().from_iterable(seq)
    assert queue.first() == queue[0] == seq[0]


def test_representations(data):
    """repr(queue) and str(queue)."""
    queue = Queue().from_iterable(data)
    assert repr(queue) == repr(data)
    assert str(queue) == str(data)


def test_less_than_operation(data):
    """self < other"""
    queue1 = Queue()
    queue2 = Queue.from_iterable(data)
    assert queue1 < queue2
    assert queue2 >= queue1


def test_iterableness(data):
    """Test the queue to be iterable."""
    for quel, datel in zip(Queue.from_iterable(data), data):
        assert quel == datel
