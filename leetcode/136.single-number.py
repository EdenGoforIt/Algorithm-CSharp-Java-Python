#
# @lc app=leetcode id=136 lang=python3
#
# [136] Single Number
#
 


# @lc code=start
from typing import List


class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        result = 0
        for num in nums:
            result ^= num
        return result
 
        
# @lc code=end

