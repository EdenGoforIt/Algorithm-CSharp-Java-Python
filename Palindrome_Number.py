
from typing import List


class Solution:
    def kapsack(self, nums: List[int], k: int) -> int:
        size = len(nums)
        maxCapacity = k
        weights = [False] * (maxCapacity+1)
        weights[0] = True
        maxValue = 0
        for i in range(1, len(nums), 1):
            temp = nums[i]
            for j in range(i+1, len(nums), 1):
                if temp + nums[j] < maxCapacity:
                    temp += nums[j]
                    maxValue = temp

        return maxValue


if __name__ == '__main__':
    nums = [1, 3, 5]
    k = 5
    test = Solution().kapsack(nums, k)
    print(test)
