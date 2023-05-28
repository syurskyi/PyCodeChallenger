from typing import List
#  Importing the List type from the typing module to annotate the function parameter and return types.


class Solution:
    # Defining a class named Solution that encapsulates the logic for finding the longest common prefix.
    def longestCommonPrefix(self, strs: List[str]) -> str:
        # Defining the method longestCommonPrefix within the Solution class. It takes a list of strings as input
        # and returns a string as the output. The self parameter refers to the instance of the class.
        if not strs:
            # Checking if the input list strs is empty.
            # If it is, there are no strings to find a common prefix among, so an empty string is returned.
            return ""

        prefix = ""
        # Initializing an empty string variable prefix to store the common prefix.
        for chars in zip(*strs):
            # Iterating through the characters of the strings in strs by using zip(*strs) to transpose
            # the strings and iterate over them character by character.
            if len(set(chars)) == 1:
                # Checking if all characters in the current position of chars are the same by converting them
                # to a set and checking if the set length is 1. If it is, it means the characters are all equal.
                prefix += chars[0]
                #  Appending the first character from the chars tuple (which is the common character)
                #  to the prefix string.
            else:
                # If the characters at the current position are not all equal,
                # it breaks out of the loop since the common prefix ends at this position.
                break

        return prefix
    # Returning the final prefix string, which contains the longest common prefix among the input strings.


class TestLongestCommonPrefix:
    @staticmethod # Decorating the run_tests method as a static method, which means
    # it can be called without creating an instance of the class.
    def run_tests():
        test_cases = [
            (["flower", "flow", "flight"], "fl"),
            (["dog", "racecar", "car"], ""),
        ]
        # Defining a list of test cases. Each test case is a tuple containing the input list strs and
        # the expected output expected.

        solution = Solution() # Creating an instance of the Solution class

        for strs, expected in test_cases:
            # Iterating through the test cases.
            result = solution.longestCommonPrefix(strs)
            # Calling the longestCommonPrefix method on the solution instance with the current input strs
            # to get the result.
            assert result == expected, f"Expected: {expected}, Got: {result}"
            # Asserting that the result matches the expected output.
            # If not, it raises an assertion error with a formatted error message.
            print(f"Input: strs={strs}")
            print("Result:", result)
            print("Expected output:", expected)
            print("Test passed:", result == expected)
            print()

        print("All test cases passed!")


if __name__ == "__main__":
    TestLongestCommonPrefix.run_tests()
