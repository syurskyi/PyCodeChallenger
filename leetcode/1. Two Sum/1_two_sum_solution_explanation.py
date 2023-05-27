# These lines import the necessary modules for the code. The typing module is used for type hints,
# and the defaultdict class is imported from the collections module.
from typing import List
from collections import defaultdict


class Solution:
    @staticmethod
    def twoSum(nums: List[int], target: int) -> List[int]: #
        # The twoSum method takes in a list of integers (nums) and a target integer (target).
        # It aims to find two numbers in the list that add up to the target and return their indices in a list.
        seen = defaultdict(int)
        # A defaultdict named seen is created with a default value of 0.
        # This dictionary will be used to store previously seen numbers and their indices.
        for i, num in enumerate(nums):
            # The method iterates over the nums list using the enumerate function to access both the indices (i)
            # and the corresponding numbers (num).
            complement = target - num
            # For each number, the complement is calculated by subtracting it from the target.
            if complement in seen:
                return [seen[complement], i]
            # If the complement is present in the seen dictionary, it means that the current number,
            # when combined with a previously seen number, adds up to the target. In this case,
            # the method returns a list containing the indices of the two numbers.
            seen[num] = i
            # If the complement is not present in seen,
            # the current number is added to seen with its corresponding index.
        return []
    # If no two numbers are found that add up to the target, an empty list is returned.


class TestSolution:
    @staticmethod
    def run_tests():
        test_cases = [
            ([2, 7, 11, 15], 9, [0, 1]),
            ([3, 2, 4], 6, [1, 2]),
            ([3, 3], 6, [0, 1]),
        ]
        # A list of test cases is defined. Each test case is a tuple containing the nums list, target value,
        # and the expected output.

        for nums, target, expected in test_cases:
            # The method iterates over the test cases using a for loop.
            result = Solution.twoSum(nums, target)
            # For each test case, the twoSum method is called with the provided nums and target values.
            # The result is stored in the result variable
            assert result == expected, f"Expected: {expected}, Got: {result}"
            # An assertion is used to check if the result matches the expected output.
            # If they don't match, an error message is raised.
            result = Solution.twoSum(nums, target)
            print(f"Input: nums={nums}, target={target}")
            print("Result:", result)
            print("Expected output:", expected)
            print("Test passed:", result == expected)
            print()

        print("All test cases passed!")


if __name__ == "__main__":
    TestSolution.run_tests()
