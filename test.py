import pytest
from position import *


def test_position_create_valid_1_2():
    assert position_create(1, 2) is not None


def test_position_create_valid_1000_0():
    assert position_create(1000, 0) is not None


def test_position_create_invalid_args_minus1():
    try:
        position_create(-1, -1)
    except ValueError as error:
        assert str(error) == 'position_create: invalid arguments'


def test_position_create_invalid_args_emptytuple():
    try:
        position_create((), ())
    except ValueError as error:
        assert str(error) == 'position_create: invalid arguments'


def test_position_is_true():
    assert position_is(position_create(1, 2)) is True
