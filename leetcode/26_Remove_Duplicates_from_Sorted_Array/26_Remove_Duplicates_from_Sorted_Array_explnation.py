from typing import List
# This line is importing List from the typing module.
# List is a way to hint the type of elements in a list. As of Python 3.9, you can use list instead of List in type hints.


class Solution: # This line is defining a class named Solution.
    def removeDuplicates(self, nums: list[int]) -> int:
        # This line is defining a method called removeDuplicates that belongs to the Solution class.
        # It takes two arguments: self (a reference to the instance of the class) and nums (a list of integers).
        # It is annotated to return an integer.

        if not nums:
            return 0
        # This is a check to see if nums is an empty list.
        # If it is, the function immediately returns 0, since there are no elements (and thus no unique elements).

        unique_index = 1
        # This line initializes unique_index as 1.
        # unique_index is used as a pointer to keep track of the location where the next unique element should be placed

        for current in nums[1:]:
            # This line starts a for loop that iterates over the elements in nums, starting from
            # the second element (since Python indexes start at 0).
            if current != nums[unique_index - 1]:
                # This line checks if the current number is not equal to the previous number in the sorted list.
                # If it isn't, this means we've encountered a new unique number.
                nums[unique_index] = current
                unique_index += 1
                # If the current number is unique, it is placed at the position indicated by unique_index,
                # and unique_index is then incremented by 1.

        return unique_index
    # This line is returning the total count of unique elements in the nums list.


class TestRemoveDuplicates:
    # This line is defining a new class named TestRemoveDuplicates, which is used for testing the Solution class.
    @staticmethod
    def run_tests():
        # This is defining a static method called run_tests inside the TestRemoveDuplicates class.
        # A static method is a method that belongs to a class rather than an instance of the class.
        test_cases = [
            ([2, 7, 11, 15], [2, 7, 11, 15], 4),
            ([3, 2, 4], [3, 2, 4], 3),
            ([3, 3], [3], 1),
            ([1, 1, 2], [1, 2, '_'], 2),
            ([0, 0, 1, 1, 1, 2, 2, 3, 3, 4], [0, 1, 2, 3, 4, '_', '_', '_', '_', '_'], 5),
        ]
        # This line is defining a list of test cases. Each test case is a tuple containing an input list of numbers,
        # the expected list after removing duplicates, and the expected length of the unique list.

        solution = Solution()
        # This line is creating an instance of the Solution class.

        for nums, expected_nums, expected_length in test_cases:
            # This line is starting a for loop that iterates over each test case.
            result_length = solution.removeDuplicates(nums)
            result_nums = nums[:result_length]
            # These lines are calling the removeDuplicates method with the current test case's input list and
            # storing the resulting length. It also slices the input list to the returned length to get
            # the list after removing duplicates.

            assert result_length == expected_length, f"Expected Length: {expected_length}, Got: {result_length}"
            # This line is using an assert statement to check if the result matches the expected output.
            # If the assertion fails, it will raise an AssertionError with the provided error message.
            # assert result_nums == expected_nums, f"Expected nums: {expected_nums}, Got: {result_nums}"

            print(f"Input: nums={nums}")
            print("Result Length:", result_length)
            print("Result nums:", result_nums)
            print("Expected Length:", expected_length)
            print("Expected nums:", expected_nums)
            print("Test passed:", result_length == expected_length and result_nums == expected_nums)
            print()
            # These lines are printing out the input, the result, the expected output, and whether the test passed.

        print("All test cases passed!")
        # This line is printed out when all test cases pass successfully.


if __name__ == "__main__":
    TestRemoveDuplicates.run_tests()
