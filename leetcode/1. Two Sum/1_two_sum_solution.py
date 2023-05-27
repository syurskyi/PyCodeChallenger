from typing import List
from collections import defaultdict


class Solution:
    @staticmethod
    def twoSum(nums: List[int], target: int) -> List[int]:
        seen = defaultdict(int)
        for i, num in enumerate(nums):
            complement = target - num
            if complement in seen:
                return [seen[complement], i]
            seen[num] = i
        return [], "No two numbers found that add up to the target."


class TestSolution:
    @staticmethod
    def run_tests():
        test_cases = [
            ([2, 7, 11, 15], 9, [0, 1]),
            ([3, 2, 4], 6, [1, 2]),
            ([3, 3], 6, [0, 1]),
        ]

        for nums, target, expected in test_cases:
            result = Solution.twoSum(nums, target)
            assert result == expected, f"Expected: {expected}, Got: {result}"
            result = Solution.twoSum(nums, target)
            print(f"Input: nums={nums}, target={target}")
            print("Result:", result)
            print("Expected output:", expected)
            print("Test passed:", result == expected)
            print()

        print("All test cases passed!")


if __name__ == "__main__":
    TestSolution.run_tests()
