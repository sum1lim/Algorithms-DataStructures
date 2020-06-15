import pytest

import numpy as np
from algorithms.quickSort import quickSort
from algorithms.radixSort import radixSort
from algorithms.bubbleSort import bubbleSort
import time


def input_expected_pair(n):
    input_arr = np.random.randint(n*10, size=(n))
    input_arr = input_arr.tolist()
    start_time = time.time()
    expected_output = sorted(input_arr)
    elapsed_time = round(time.time() - start_time, 5)
    print("\n default python sort(): " + str(elapsed_time) + "sec" + " for size " + str(n))
    return (input_arr, expected_output)

parameters_li = [input_expected_pair(size) for size in [1000, 2000, 4000, 8000, 16000]]

@pytest.mark.parametrize(
    ("input_arr", "expected_output"),
    parameters_li,
)
def test_bubbleSort(input_arr, expected_output):
    start_time = time.time()
    bubbleSort(input_arr)
    elapsed_time = round(time.time() - start_time, 5)
    print("\n Bubble Sort: " + str(elapsed_time) + "sec" + " for size " + str(len(input_arr))
            + "\n   -----> " + str(len(input_arr)) + " = " + str(int(len(input_arr)/2)) + " * 2"
            + "\n   -----> " + str(elapsed_time) + " = " + str(elapsed_time/4) + " * 2^2"
            + "\n   -----> O(n^2)")
    assert (input_arr == expected_output)


@pytest.mark.parametrize(
    ("input_arr", "expected_output"),
    parameters_li,
)
def test_quickSort(input_arr, expected_output):
    start_time = time.time()
    quickSort(input_arr)
    elapsed_time = round(time.time() - start_time, 5)
    print("\n Quick Sort: " + str(elapsed_time) + "sec" + " for size " + str(len(input_arr)))
    assert (input_arr == expected_output)

@pytest.mark.parametrize(
    ("input_arr", "expected_output"),
    parameters_li,
)
def test_quickSort_LDS(input_arr, expected_output):
    start_time = time.time()
    quickSort(input_arr, LDS = True)
    elapsed_time = round(time.time() - start_time, 5)
    print("\n Quick Sort(Linear Deterministic Selection): " + str(elapsed_time) + "sec" + " for size " + str(len(input_arr)))
    assert (input_arr == expected_output)

@pytest.mark.parametrize(
    ("input_arr", "expected_output"),
    parameters_li,
)
def test_radixSort(input_arr, expected_output):
    start_time = time.time()
    radixSort(input_arr)
    elapsed_time = round(time.time() - start_time, 5)
    print("\n Radix Sort: " + str(elapsed_time) + "sec" + " for size " + str(len(input_arr)))
    assert (input_arr == expected_output)