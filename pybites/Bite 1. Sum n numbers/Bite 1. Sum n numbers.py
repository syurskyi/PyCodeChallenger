from typing import List


class NumberSummer:
    def __init__(self):
        self.default_numbers = list(range(1, 101))

    def calculate_sum(self, numbers: List[int] = None) -> int:
        numbers = numbers or self.default_numbers
        return sum(numbers)


class TestNumberSummer:
    @staticmethod
    def run_tests():
        test_cases = [
            ([2, 4, 6, 8, 10], 30),
            (None, 5050),
        ]

        summer = NumberSummer()

        for numbers, expected in test_cases:
            result = summer.calculate_sum(numbers)
            assert result == expected, f"Expected: {expected}, Got: {result}"
            print(f"Input: numbers={numbers}")
            print("Result:", result)
            print("Expected output:", expected)
            print("Test passed:", result == expected)
            print()

        print("All test cases passed!")


if __name__ == "__main__":
    TestNumberSummer.run_tests()