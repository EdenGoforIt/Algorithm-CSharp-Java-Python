#
# @lc app=leetcode id=268 lang=python3
#
# [268] Missing Number
#
from typing import List


# @lc code=start
class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        # n = len(nums)
        # expected_sum = n * (n + 1) // 2
        # actual_sum = sum(nums)
        # return expected_sum - actual_sum
        res = len(nums)
        for i, num in enumerate(nums):
            res ^= i ^ num
        return res


# @lc code=end
