class Solution: # Defines a class named Solution.
    def isPalindrome(self, x: int) -> bool: #  Defines a method isPalindrome that takes an integer x as input
        # and returns a boolean value.
        if x < 0 or (x % 10 == 0 and x != 0):
            # Checks if x is negative or if it ends with a zero but is not zero itself.
            # If either condition is true, it means x is not a palindrome, and the method returns False.
            return False

        reversed_num = 0 # Initializes a variable reversed_num to store the reversed number.
        while x > reversed_num:
            #  Enters a while loop that continues until x becomes less than or equal to reversed_num.
            reversed_num = reversed_num * 10 + x % 10
            #  Inside the loop, the last digit of x (obtained using x % 10) is appended to reversed_num
            #  after multiplying reversed_num by 10. This effectively builds the reversed number.
            x //= 10 #  After extracting the last digit, x is updated by integer division (//) to remove the last digit.

        return x == reversed_num or x == reversed_num // 10
    # After exiting the loop, checks if x is equal to reversed_num or reversed_num divided by 10
    # (to handle the case of odd-length palindromes where the middle digit can be ignored).


class TestSolution:
    @staticmethod
    def run_tests():
        test_cases = [
            (121, True),
            (-121, False),
            (10, False),
            (12321, True),
            (12345678987654321, True),
        ] # Defines a list of test cases, each containing an input value x and the expected output value.

        solution = Solution()  # Creates an instance of the Solution class.

        for x, expected in test_cases: # Iterates over each test case.
            result = solution.isPalindrome(x)
            #  Calls the isPalindrome() method of the Solution instance with the current input value x
            #  and assigns the result to result.
            assert result == expected, f"Expected: {expected}, Got: {result}"
            #  Asserts that the result matches the expected output. If the assertion fails, an error message is displayed.
            print(f"Input: x={x}")
            print("Result:", result)
            print("Expected output:", expected)
            print("Test passed:", result == expected) #  Prints whether the test passed or not.
            print()

        print("All test cases passed!")


if __name__ == "__main__":
    TestSolution.run_tests()
