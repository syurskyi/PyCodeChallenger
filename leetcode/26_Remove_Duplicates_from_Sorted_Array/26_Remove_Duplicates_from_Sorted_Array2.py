class Solution:
    def removeDuplicates(self, nums):
        """
        This function removes duplicates from a sorted array and returns the number of unique elements.

        :param nums: a sorted list of integers
        :return: the number of unique integers
        """
        if not nums:
            return 0

        unique_index = 1

        for current in nums[1:]:
            if current != nums[unique_index - 1]:
                nums[unique_index] = current
                unique_index += 1

        return unique_index


# Testing the Solution:

solution = Solution()

# Test 1
nums1 = [1,1,2]
expected_output1 = 2
assert solution.removeDuplicates(nums1) == expected_output1, f"Expected {expected_output1}, but got {solution.removeDuplicates(nums1)}"

# Test 2
nums2 = [0,0,1,1,1,2,2,3,3,4]
expected_output2 = 5
assert solution.removeDuplicates(nums2) == expected_output2, f"Expected {expected_output2}, but got {solution.removeDuplicates(nums2)}"

print("All tests passed!")
