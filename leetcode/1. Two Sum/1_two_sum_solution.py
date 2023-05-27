from typing import List
from collections import defaultdict


class TwoSumFinder:
    @staticmethod
    def twoSum(nums: List[int], target: int) -> List[int]:
        seen = defaultdict(int)
        for index, num in enumerate(nums):
            complement = target - num
            if complement in seen:
                return [seen[complement], index]
            seen[num] = index
        return [], "No two numbers found that add up to the target."


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
