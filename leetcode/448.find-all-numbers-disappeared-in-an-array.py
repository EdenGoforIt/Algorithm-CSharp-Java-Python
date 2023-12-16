#
# @lc app=leetcode id=448 lang=python3
#
# [448] Find All Numbers Disappeared in an Array
#


# @lc code=start
from typing import List


class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        set_num = set(nums)
        result = []
        for i in range(1, len(nums) + 1):
            if i not in set_num:
                result.append(i)

        return result


Solution().findDisappearedNumbers([1, 1])
# @lc code=end
