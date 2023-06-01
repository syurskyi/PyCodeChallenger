from typing import List
# This line imports List from the typing module, a standard Python library for specifying the data types of variables,
# function arguments, and return values in a more complex way than just int, str, etc.
# It's often used to enhance the clarity of code and allow better static analysis
# (i.e., checking of types before the program is run).


class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        # This line defines a method named removeElement inside the Solution class. This method takes three parameters:
        # self, nums, and val. The self keyword is a reference to the instance of the class and is used
        # to access variables that belongs to the class. The nums parameter is a list of integers (List[int]),
        # and val is an integer (int). The -> int at the end signifies that this function returns an integer.
        new_list_pointer = 0
        # This line initializes a variable new_list_pointer to 0. This variable will be used to track
        # the new length of the list after removing elements.

        for num in nums:
            # This line starts a loop that iterates over each number in the nums list.
            if num != val:
                # This line checks if the current number in the loop is not equal to the value specified by val.
                nums[new_list_pointer] = num
                # If the number isn't equal to val, this line assigns the number to the new_list_pointer index of nums.
                new_list_pointer += 1
                # If the number isn't equal to val, this line increments new_list_pointer by 1.

        return new_list_pointer
    # Once the loop has finished, this line returns the final value of new_list_pointer,
    # which is the length of the list after all instances of val have been removed.


class TestRemoveElement:
    # This is the declaration of a new class named TestRemoveElement.
    # This class is used to test the removeElement method.
    @staticmethod
    # This decorator indicates that the following function is a static method, which is a method that belongs
    # to a class rather than an instance of a class.
    def run_tests():
        # This line defines a static method named run_tests inside the TestRemoveElement class.
        test_cases = [
            ([3, 2, 2, 3], 3, 2, [2, 2]),
            ([0, 1, 2, 2, 3, 0, 4, 2], 2, 5, [0, 1, 4, 0, 3])
        ]
        # This line defines a list of test cases. Each test case is a tuple containing a list of numbers (nums),
        # a number to remove (val), the expected length of the list after removing the numbers (expected_length),
        # and the expected list after removing the numbers (expected_nums).

        solution = Solution()
        # This line creates a new instance of the Solution class.

        for nums, val, expected_length, expected_nums in test_cases:
            # This line starts a loop that iterates over each test case in the test_cases list.
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

