import pytest
from max_subarray import max_subarray


def test_basic_example():
    array = [-2, 1, -3, 4, -1, 2, 1, -5, 4]
    assert max_subarray(array) == 6

def test_basic_only_negatives():
    array = [-2, -9, -3]
    assert max_subarray(array) == -11

def test_basic_smallest_array():
    array = [2, 4]
    assert max_subarray(array) == 6

