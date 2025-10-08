#
# @lc app=leetcode id=303 lang=python3
#
# [303] Range Sum Query - Immutable
#
from typing import List


# @lc code=start
class NumArray:
    def __init__(self, nums: List[int]):
        # nums = [3, 1, 2]
        # sum = [0, 3, 4, 6]
        # e.g if we want to get sum from index 0 to 2
        # we can just do sum[2 + 1] - sum[0] = 6 - 0 = 6
        # adding extra 0 at the beginning to avoid out of index

        # prefix sum array
        self.sum = [0] * (len(nums) + 1)
        for i in range(len(nums)):
            self.sum[i + 1] = self.sum[i] + nums[i]

    def sumRange(self, left: int, right: int) -> int:
        return self.sum[right + 1] - self.sum[left]


# Your NumArray object will be instantiated and called as such:
# obj = NumArray(nums)
# param_1 = obj.sumRange(left,right)
# @lc code=end
