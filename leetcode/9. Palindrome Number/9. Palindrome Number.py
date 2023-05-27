class Solution:
    @staticmethod
    def isPalindrome(num: int) -> bool:
        if num < 0 or (num % 10 == 0 and num != 0):
            return False

        reversed_num = 0
        original_x = num

        while num > 0:
            reversed_num = (reversed_num * 10) + (num % 10)
            num //= 10

        return original_x == reversed_num


class TestSolution:
    @staticmethod
    def run_tests():
        test_cases = [
            (121, True),
            (-121, False),
            (10, False),
            (12321, True),
            (12345678987654321, True),
        ]

        for num, expected in test_cases:
            result = Solution.isPalindrome(num)
            assert result == expected, f"Expected: {expected}, Got: {result}"
            print(f"Input: num={num}")
            print("Result:", result)
            print("Expected output:", expected)
            print("Test passed:", result == expected)
            print()

        print("All test cases passed!")


if __name__ == "__main__":
    TestSolution.run_tests()
