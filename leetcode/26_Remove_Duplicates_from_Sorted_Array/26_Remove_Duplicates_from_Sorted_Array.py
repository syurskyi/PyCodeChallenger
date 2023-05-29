from typing import List


class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        if not nums:
            return 0

        k = 1  # Number of unique elements
        current = 1  # Current index for placing unique elements

        for i in range(1, len(nums)):
            if nums[i] != nums[i - 1]:
                nums[current] = nums[i]
                k += 1
                current += 1

        return k


class TestRemoveDuplicates:
    @staticmethod
    def run_tests():
        test_cases = [
            ([2, 7, 11, 15], [2, 7, 11, 15], 4),
            ([3, 2, 4], [3, 2, 4], 3),
            ([3, 3], [3], 1),
            ([1, 1, 2], [1, 2, '_'], 2),
            ([0, 0, 1, 1, 1, 2, 2, 3, 3, 4], [0, 1, 2, 3, 4, '_', '_', '_', '_', '_'], 5),
        ]

        solution = Solution()

        for nums, expected_nums, expected_length in test_cases:
            result_length = solution.removeDuplicates(nums)
            result_nums = nums[:result_length]

            assert result_length == expected_length, f"Expected Length: {expected_length}, Got: {result_length}"
            assert result_nums == expected_nums, f"Expected nums: {expected_nums}, Got: {result_nums}"

            print(f"Input: nums={nums}")
            print("Result Length:", result_length)
            print("Result nums:", result_nums)
            print("Expected Length:", expected_length)
            print("Expected nums:", expected_nums)
            print("Test passed:", result_length == expected_length and result_nums == expected_nums)
            print()

        print("All test cases passed!")


if __name__ == "__main__":
    TestRemoveDuplicates.run_tests()
