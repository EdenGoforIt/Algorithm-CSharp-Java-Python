from typing import List


class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        dict = {}
        for i in range(len(nums)):
            left_over = target - nums[i]
            if left_over in dict.keys():
                return [dict[left_over], i]
            else:
                dict[nums[i]] = i


print(Solution().twoSum([2, 7, 11, 15], 9))
