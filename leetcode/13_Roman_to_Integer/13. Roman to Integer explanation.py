class Solution:
    # The Solution class is defined with a static method romanToInt
    # that takes a string s as input and returns an integer.
    @staticmethod
    def romanToInt(roman_numeral: str) -> int:
        # Inside the romanToInt method, a dictionary roman_to_int is defined.
        # It maps Roman numeral characters to their corresponding integer values.
        roman_to_int = {
            'I': 1,
            'V': 5,
            'X': 10,
            'L': 50,
            'C': 100,
            'D': 500,
            'M': 1000
        }

        result = 0 # Initialize a variable result to store the final converted integer value.

        for index in range(len(roman_numeral) - 1):
            # Iterate over the characters of the input string s, except the last character.
            # The loop variable index represents the current index.
            current_value = roman_to_int[roman_numeral[index]]
            # Retrieve the integer value of the current character roman_numeral[index]
            # from the roman_to_int dictionary and store it in current_value.
            next_value = roman_to_int[roman_numeral[index + 1]]
            # Retrieve the integer value of the next character roman_numeral[index + 1]
            # from the roman_to_int dictionary and store it in next_value.
            result += current_value if current_value >= next_value else -current_value
            # Compare current_value with next_value to determine whether to add or subtract the current value
            # from the result.
            #
            #     If current_value is greater than or equal to next_value, add current_value to the result.
            #     Otherwise, subtract current_value from the result.

        result += roman_to_int[roman_numeral[-1]]  # Add the value of the last character
        # Add the value of the last character roman_numeral[-1] to the result.

        return result # Return the final converted integer value.

class TestSolution:
    # The TestSolution class is defined to contain the test cases for the Solution class.
    @staticmethod
    def run_tests():
        # Inside the run_tests static method, a list of test cases is defined. Each test case consists
        # of an input string s and the expected output.
        test_cases = [
            ("III", 3),
            ("LVIII", 58),
            ("MCMXCIV", 1994),
        ]

        for roman_numeral, expected in test_cases:
            # Iterate over the test cases.
            result = Solution.romanToInt(roman_numeral)
            # For each test case, call the romanToInt method of the Solution class with the input string s and
            # store the result in result.
            assert result == expected, f"Expected: {expected}, Got: {result}"
            # Check if the result matches the expected output.
            # If not, raise an assertion error with a custom error message.
            print(f"Input: roman_numeral={roman_numeral}")
            print("Result:", result)
            print("Expected output:", expected)
            print("Test passed:", result == expected)
            print()

        print("All test cases passed!")


if __name__ == "__main__":
    TestSolution.run_tests()