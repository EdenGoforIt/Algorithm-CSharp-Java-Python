#
# @lc app=leetcode id=16 lang=python3
#
# [16] 3Sum Closest
# 
# from typing import List
# @lc code=start


class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        length = len(nums)
        sum = nums[0] + nums[1] + nums[2]
        nums.sort()

        for i in range(length - 2):
            pivot = nums[i]
            start = i + 1
            end = length-1

            while (start < end):
                current = pivot + nums[start] + nums[end]
                if current < target:
                    start += 1
                else:
                    end -= 1
                if abs(current - target) < abs(sum - target):
                    sum = current

        return sum


# print(Solution().threeSumClosest([-1, 2, 1, -4], 1))

# @lc code=end
