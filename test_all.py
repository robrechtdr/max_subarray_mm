import pytest
from max_subarray import max_subarray, max_subarray_var1, max_subarray_var2


# Basic cases
def test_basic_example():
    array = [-2, 1, -3, 4, -1, 2, 1, -5, 4]
    assert max_subarray(array) == 6

def test_basic_only_negatives():
    array = [-2, -9, -3]
    assert max_subarray(array) == -11

def test_basic_smallest_array():
    array = [2, -1]
    assert max_subarray(array) == 1

# Variation 1 cases
def test_var1_example():
    array = [-2, 1, -3, 4, -1, 2, 1, -5, 4]
    assert max_subarray_var1(array) == 6

def test_var1_only_negatives():
    array = [-2, -9, -3]
    assert max_subarray_var1(array) == -2

def test_var1_smallest_array():
    array = [2, -1]
    assert max_subarray_var1(array) == 2

# Variation 2 cases
def test_var2_example():
    array = [-2, 1, -3, 4, -1, 2, 1, -5, 4]
    assert max_subarray_var2(
        array=array,
        bitmask=[1, 1, 0, 0],
        bitmask_start_i=3
    ) == 3

def test_var2_bitmask_no_effect_on_underlying_max_array_selection():
    array = [-2, -9, -3]
    assert max_subarray_var2(
        array=array,
        bitmask=[0, 0],
        bitmask_start_i=1
    ) == -2

def test_var2_no_bitmask_args():
    array = [-2, -9, -3]
    assert max_subarray_var2(array=array) == -2


def test_var2_bitmask_larger_than_array():
    array = [-2, -9, -3]
    assert max_subarray_var2(
        array=array,
        bitmask=[0, 0, 0, 0],
        bitmask_start_i=1
    ) == -2