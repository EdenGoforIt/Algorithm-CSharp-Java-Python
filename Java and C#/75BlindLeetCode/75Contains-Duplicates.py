from typing import List


class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        dict = {}
        for i in range(len(nums)):
            if nums[i] not in dict.keys():
                dict[nums[i]] = i
            else:
                return True

        return False

    def containsDuplicate2(self, nums: List[int]) -> bool:

        return len(set(nums)) != len(nums)


print(Solution().containsDuplicate([1, 2, 3, 1]))
