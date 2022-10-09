from math import inf, isinf
from numbers import Number


def validate_input_data(array: list[Number], k: int):
    """
    Basic validation of input data

    Parameters
    ----------
    array : list of numbers, required
    k : int number, required

    Raises
    ------
    ValueError
        If any value is invalid
    """

    if not isinstance(array, list):
        raise ValueError("'array' must be a type of 'list'")
    if not isinstance(k, int):
        raise ValueError("'k' must be a type of 'int'")
    if not array:
        raise ValueError("'array' must not be empty")
    if k <= 0:
        raise ValueError("'k' must be bigger than 0")
    if k > len(array):
        raise ValueError("'k' must not be bigger than 'array' length")


def find_lowest_unfairness_value(array: list[Number], k: int) -> Number:
    """
    Min-max search method for sub-arrays with specified length

    Parameters
    ----------
    array : list of numbers, required
        defines array for min-max search
    k : int number, required
        defines sub-array length for min-max search

    Raises
    ------
    ValueError
        If min-max value was not found

    Returns
    -------
    Lowest min-max value
    """

    # Input data validation
    validate_input_data(array, k)

    # Array sorting reduces sub-array combinations to only relevant ones
    sorted_arr = sorted(array)
    # Reducing len() call by 1
    length_arr = len(sorted_arr)

    # Initial value for comparison
    lowest_unfairness = inf

    # No sub-arrays are needed when array == sub-array
    if k == length_arr:
        lowest_unfairness = sorted_arr[-1] - sorted_arr[0]
    # Case with sub-arrays formation
    else:
        # Moving static math operation out loop
        k_index = k - 1
        for begin_index in range(0, length_arr - k):
            end_index = begin_index + k_index
            curr_unfairness = sorted_arr[end_index] - sorted_arr[begin_index]
            if curr_unfairness < lowest_unfairness:
                lowest_unfairness = curr_unfairness

    if isinf(lowest_unfairness):
        raise ValueError("Could not find a valid unfairness value")

    return lowest_unfairness


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
