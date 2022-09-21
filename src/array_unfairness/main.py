from math import inf, isinf
from numbers import Number


def find_lowest_unfairness_value(array: list[Number], k: int) -> Number:
    # Basic parameters checks
    if not isinstance(array, list):
        raise ValueError("'array' should be a type of list")
    if not isinstance(k, int):
        raise ValueError("'k' should be a type of int")
    if not array:
        raise ValueError("'array' should not be empty")
    if k <= 0:
        raise ValueError("'k' value must be bigger than 0")
    if k > len(array):
        raise ValueError("'k' should not be bigger than array length")

    # Array sorting reduces sub-array combinations to only relevant ones
    sorted_arr = sorted(array)

    # If no sub-arrays are needed when array == sub-array
    if k == len(array):
        return sorted_arr[-1] - sorted_arr[0]

    lowest_unfairness = inf
    k_index = k - 1
    for begin_index in range(0, len(array) - k):
        end_index = begin_index + k_index
        curr_unfairness = sorted_arr[end_index] - sorted_arr[begin_index]
        if curr_unfairness < lowest_unfairness:
            lowest_unfairness = curr_unfairness

    if isinf(lowest_unfairness):
        raise ValueError("Could not find a valid unfairness value")

    return lowest_unfairness


# Applicable to unsorted sub-array
# def calculate_unfairness(arr: list[Number]) -> Number:
#    if not array:
#        raise ValueError("Array should not be empty")
#
#    # First option
#    # sorted_arr = sorted(arr)
#    # return sorted_arr[0] - sorted_arr[-1]
#
#    # Second option
#    return max(arr) - min(arr)

if __name__ == "__main__":
    # Sample data
    array = [1, 4, 7, 2]
    k = 2

    # All possible combinations (without swapped duplicates)
    # 1, 4 -> 3
    # 1, 7 -> 6
    # 1, 2 -> 1
    # 4, 7 -> 3
    # 4, 2 -> 2
    # 7, 2 -> 5
    # Lowest value = 1

    print(
        f"Input data:\n"
        f"  array = {array}\n"
        f"  k = {k}\n"
        f"Result = {find_lowest_unfairness_value(array, k)}"
    )
