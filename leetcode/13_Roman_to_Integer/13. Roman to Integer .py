class Solution:
    @staticmethod
    def romanToInt(roman_numeral: str) -> int:
        roman_to_int = {
            'I': 1,
            'V': 5,
            'X': 10,
            'L': 50,
            'C': 100,
            'D': 500,
            'M': 1000
        }

        result = 0

        for index in range(len(roman_numeral) - 1):
            current_value = roman_to_int[roman_numeral[index]]
            next_value = roman_to_int[roman_numeral[index + 1]]
            result += current_value if current_value >= next_value else -current_value

        result += roman_to_int[roman_numeral[-1]]  # Add the value of the last character

        return result


class TestSolution:
    @staticmethod
    def run_tests():
        test_cases = [
            ("III", 3),
            ("LVIII", 58),
            ("MCMXCIV", 1994),
        ]

        for roman_numeral, expected in test_cases:
            result = Solution.romanToInt(roman_numeral)
            assert result == expected, f"Expected: {expected}, Got: {result}"
            print(f"Input: roman_numeral={roman_numeral}")
            print("Result:", result)
            print("Expected output:", expected)
            print("Test passed:", result == expected)
            print()

        print("All test cases passed!")


if __name__ == "__main__":
    TestSolution.run_tests()