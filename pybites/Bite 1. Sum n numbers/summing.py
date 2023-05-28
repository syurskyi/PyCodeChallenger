from typing import List


def sum_numbers(numbers: List[int] = None) -> int:
    default_numbers = list(range(1, 101))
    if numbers is None:
        numbers = default_numbers
    return sum(numbers)

