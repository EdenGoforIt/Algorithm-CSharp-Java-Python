class Solution(object):
    def twoSum(nums, target):
        dict = {}
        for i in len(nums):
            first_value = nums[i]
            second_value = target-first_value
            if(first_value > target or second_value > target):
                continue

            if second_value in dict.keys:


print(Solution.twoSum([2, 19, 7, 5, 15], 9))
print(Solution.twoSum([3, 2, 4], 6))
print(Solution.twoSum([3, 3], 6))


# https: // leetcode.com/problems/two-sum/
