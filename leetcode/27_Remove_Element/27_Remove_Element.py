from typing import List


class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        slow = 0

        for fast in range(len(nums)):
            if nums[fast] != val:
                nums[slow] = nums[fast]
                slow += 1

        return slow

solution = Solution()

nums = [3,2,2,3]
val = 3
print(solution.removeElement(nums, val))  # Output: 2

nums = [0,1,2,2,3,0,4,2]
val = 2
print(solution.removeElement(nums, val))  # Output: 5
