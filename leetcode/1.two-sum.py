#
# @lc app=leetcode id=1 lang=python3
#
# [1] Two Sum
#
from typing import List
# @lc code=start


class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        dict = {}

        for i in range(len(nums)):
            first_value = nums[i]
            second_value = target-first_value 

            if second_value in dict.keys():
                return [dict[second_value], i]
            else:
                dict[first_value] = i


print(Solution().twoSum([-3, 4, 3, 90], 0)) 

# @lc code=end
