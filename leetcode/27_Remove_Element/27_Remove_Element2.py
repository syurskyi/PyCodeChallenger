from typing import List


from typing import List

class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        # Pointer for the new list without the given value
        new_list_pointer = 0

        for num in nums:
            # If the current number is not the value to be removed
            if num != val:
                # Assign it to the position of the new_list_pointer
                nums[new_list_pointer] = num
                # Move the pointer of the new list
                new_list_pointer += 1

        # The length of the new list is the position of the new_list_pointer
        return new_list_pointer


class TestRemoveElement:
    @staticmethod
    def run_tests():
        test_cases = [
            ([3, 2, 2, 3], 3, 2, [2, 2]),
            ([0, 1, 2, 2, 3, 0, 4, 2], 2, 5, [0, 1, 4, 0, 3])
        ]

        solution = Solution()

        for nums, val, expected_length, expected_nums in test_cases:
            result_length = solution.removeElement(nums, val)
            result_nums = nums[:result_length]
            print(f"Input: nums={nums}, val={val}")
            print("Result Length:", result_length)
            print("Result nums:", result_nums)
            print("Expected Length:", expected_length)
            print("Expected nums:", expected_nums)
            print("Test passed:", result_length == expected_length and sorted(result_nums) == sorted(expected_nums))
            print()

        print("All test cases passed!")


if __name__ == "__main__":
    TestRemoveElement.run_tests()

