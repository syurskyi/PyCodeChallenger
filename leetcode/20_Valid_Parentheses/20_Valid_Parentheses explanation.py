class Solution:
    # The Solution class defines a method isValid that takes a string parentheses_string as input and returns
    # a boolean indicating whether the parentheses in the string are valid or not.
    def isValid(self, parentheses_string: str) -> bool:
        stack = []
        # stack is initialized as an empty list. It will be used to keep track
        # of opening parentheses encountered in the parentheses_string.
        mapping = {')': '(', '}': '{', ']': '['}
        # mapping is a dictionary that maps closing parentheses to their corresponding opening parentheses.
        # It is used to check if the encountered closing parentheses are valid

        for char in parentheses_string:
            # The code iterates over each character char in the parentheses_string.
            if char in mapping:
                if not stack or stack[-1] != mapping[char]:
                    # if char is a closing parentheses (found in the mapping), it checks if the stack is empty or
                    # if the topmost element of the stack (last opening parentheses encountered)
                    # is not the corresponding opening parentheses for the current char.
                    return False
                #  If either condition is true, it returns False indicating an invalid parentheses configuration.
                stack.pop()
                #  Otherwise, it removes the topmost element from the stack using stack.pop().
            else:
                stack.append(char)
                # If char is not a closing parentheses, it means it is an opening parentheses,
                # so it is added to the stack using stack.append(char).

        return not stack
    # Finally, after iterating through all characters in the parentheses_string, if the stack is empty,
    # it means all opening parentheses have been properly closed, and the function returns True. Otherwise,
    # it returns False.


class TestValidParentheses:
    @staticmethod
    def run_tests():
        test_cases = [
            ("()", True),
            ("()[]{}", True),
            ("(]", False),
        ]

        solution = Solution()

        for parentheses_string, expected in test_cases:
            # The for loop iterates over each test case, calling the isValid method with the parentheses string and
            # comparing the result with the expected output.
            result = solution.isValid(parentheses_string)
            assert result == expected, f"Expected: {expected}, Got: {result}"
            print(f"Input: parentheses_string='{parentheses_string}'")
            print("Result:", result)
            print("Expected output:", expected)
            print("Test passed:", result == expected)
            print()

        print("All test cases passed!")


if __name__ == "__main__":
    TestValidParentheses.run_tests()