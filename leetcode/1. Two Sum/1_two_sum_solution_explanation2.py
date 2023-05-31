from typing import List
from collections import defaultdict


class TwoSumFinder:
    @staticmethod
    def twoSum(nums: List[int], target: int) -> List[int]:
        seen = defaultdict(int) # Create an empty dictionary seen.
        for index, num in enumerate(nums): # For each number in the list nums (indexed by index):
            complement = target - num # a. Calculate its complement with respect to the target,
            # i.e., complement = target - num.
            if complement in seen:
                # If the complement is in seen already (i.e., we have encountered a number before that,
                # if added to the current number, would equal the target),
                return [seen[complement], index]
            # return a list of the index of the complement and the index.
            seen[num] = index
            # Otherwise, add the current number and its index to the seen dictionary.
        return [], "No two numbers found that add up to the target."
    # If no such pair of numbers is found after examining the entire list,
    # return an empty list along with a message indicating the situation.

# Start:
#   Input: nums[], target
#   seen = {}
#
#   for index, num in nums:
#     calculate: complement = target - num
#     if complement in seen:
#       Success: return [seen[complement], index]
#     else:
#       seen[num] = index
#
#   Failure: return [], "No two numbers found that add up to the target."
# End

# This algorithm has a time complexity of O(n) where n is the length of the input list nums, as it traverses
# the list only once. The space complexity is also O(n) in the worst case, as in the situation where no pair
# sums to the target, we would end up storing all the n elements of nums in the seen dictionary.


class TestTwoSumFinder:
    @staticmethod
    def run_tests():
        test_cases = [
            ([2, 7, 11, 15], 9, [0, 1]),
            ([3, 2, 4], 6, [1, 2]),
            ([3, 3], 6, [0, 1]),
        ]

        for nums, target, expected in test_cases:
            result = TwoSumFinder.twoSum(nums, target)
            assert result == expected, f"Expected: {expected}, Got: {result}"
            result = TwoSumFinder.twoSum(nums, target)
            print(f"Input: nums={nums}, target={target}")
            print("Result:", result)
            print("Expected output:", expected)
            print("Test passed:", result == expected)
            print()

        print("All test cases passed!")


if __name__ == "__main__":
    TestTwoSumFinder.run_tests()
