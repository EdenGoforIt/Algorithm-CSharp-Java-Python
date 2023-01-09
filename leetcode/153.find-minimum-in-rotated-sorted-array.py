#
# @lc app=leetcode id=153 lang=python3
#
# [153] Find Minimum in Rotated Sorted Array
#
from typing import List

# @lc code=start


class Solution:
    def findMin(self, nums: List[int]) -> int:

        left = 0
        right = len(nums) - 1

        while left < right:
            mid = left + (right - left) // 2

            if nums[mid] > nums[mid + 1]:
                return nums[mid+1]

            if nums[mid - 1] > nums[mid]:
                return nums[mid]

            if nums[0] < nums[mid]:
                left = mid + 1
            else:  # 4 < 1
                right = mid - 1

        return nums[0]


print(Solution().findMin([11, 13, 15, 17]))

# @lc code=end
