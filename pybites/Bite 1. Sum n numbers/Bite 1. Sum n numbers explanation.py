from typing import List
#  Importing the List type hint from the typing module. This is used to specify the type of
#  the numbers parameter in the NumberSummer class.


class NumberSummer:
    def __init__(self):
        # The __init__ method is a special method that initializes the NumberSummer object. In this case, it sets
        # the self.default_numbers instance variable to a list containing numbers 1 to 100.
        self.default_numbers = list(range(1, 101))

    def calculate_sum(self, numbers: List[int] = None) -> int:
        # Defining the calculate_sum method. It takes a list of integers as the numbers parameter
        # (with a default value of None) and returns an integer.
        # If numbers is None, it assigns self.default_numbers to numbers.
        # Then it calculates the sum of the numbers list using the sum function and returns the result.
        numbers = numbers or self.default_numbers
        return sum(numbers)


class TestNumberSummer:
    @staticmethod
    def run_tests():
        # The run_tests static method of the TestNumberSummer class. It contains a list of test_cases where
        # each test case is a tuple containing numbers and the expected sum (expected).
        # It creates an instance of the NumberSummer class called summer.
        test_cases = [
            ([2, 4, 6, 8, 10], 30),
            (None, 5050),
        ]

        summer = NumberSummer()

        for numbers, expected in test_cases:
            result = summer.calculate_sum(numbers)
            # Calls the calculate_sum method on the summer object with the numbers from the current test case.
            assert result == expected, f"Expected: {expected}, Got: {result}"
            # Compares the result with the expected value and raises an assertion error if they don't match.
            print(f"Input: numbers={numbers}")
            print("Result:", result)
            print("Expected output:", expected)
            print("Test passed:", result == expected)
            print()

        print("All test cases passed!")


if __name__ == "__main__":
    TestNumberSummer.run_tests()

# The code defines a NumberSummer class with an __init__ method to initialize the default numbers and
# a calculate_sum method to calculate the sum of a list of numbers.
# It also includes a TestNumberSummer class with a run_tests method to test the calculate_sum method.
# When the script is run, the tests are executed to ensure the correctness of the NumberSummer class.