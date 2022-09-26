import runpy
import warnings
from math import inf

import pytest

from src.array_unfairness.main import find_lowest_unfairness_value


@pytest.mark.parametrize(
    "test_data",
    [
        {"arr": [1], "k": 1, "exp_res": 0},
        {"arr": [1, 4, 7, 2], "k": 1, "exp_res": 0},
        {"arr": [1, 4, 7, 2], "k": 2, "exp_res": 1},
        {"arr": [1, 4, 7, 2], "k": 3, "exp_res": 3},
        {"arr": [1, 4, 7, 2], "k": 4, "exp_res": 6},
    ],
)
def test_find_lowest_unfairness_value(test_data):
    arr = test_data["arr"]
    k = test_data["k"]
    exp_res = test_data["exp_res"]
    assert exp_res == find_lowest_unfairness_value(arr, k)


@pytest.mark.parametrize(
    "test_data",
    [
        # None values
        {"arr": None, "k": 1},
        {"arr": [1, 2, 3], "k": None},
        # Empty "array" list
        {"arr": [], "k": 1},
        # Invalid "k" value
        {"arr": [1, 2, 3], "k": -1},
        {"arr": [1, 2, 3], "k": 0},
        {"arr": [1, 2, 3], "k": 4},
    ],
)
@pytest.mark.xfail(raises=ValueError)
def test_invalid_data_find_lowest_unfairness_value(test_data):
    arr = test_data["arr"]
    k = test_data["k"]
    find_lowest_unfairness_value(arr, k)


@pytest.mark.xfail(raises=ValueError)
def test_not_found_value_find_lowest_unfairness_value():
    arr = [inf, inf, inf, inf]
    k = 3
    find_lowest_unfairness_value(arr, k)


def test_module_run_main():
    # TODO: fix runtime warning
    warnings.filterwarnings(
        "ignore",
        category=RuntimeWarning,
        message="'src.array_unfairness.main' found in sys.modules",
    )
    runpy.run_module("src.array_unfairness.main", run_name="__main__")
