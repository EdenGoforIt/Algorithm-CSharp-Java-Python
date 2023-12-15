# 485. Max Consecutive Ones
# Easy

# 1492

# 388

# Add to List

# Share
# Given a binary array nums, return the maximum number of consecutive 1's in the array.


# Example 1:

# Input: nums = [1,1,0,1,1,1]
# Output: 3
# Explanation: The first two digits or the last three digits are consecutive 1s. The maximum number of consecutive 1s is 3.
# Example 2:

# Input: nums = [1,0,1,1,0,1]
# Output: 2


# Constraints:

# 1 <= nums.length <= 105
# nums[i] is either 0 or 1.


import datetime
from typing import List


class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:

        if len(nums) == 0:
            return 0

        longest = 0
        count = 0
        for i in range(0, len(nums), 1):
            if 1 == nums[i]:
                count = count + 1
                if longest < count:
                    longest = count
            else:
                count = 0

        return longest


if __name__ == '__main__':
    test1 = Solution().findMaxConsecutiveOnes([1, 1, 0, 1, 1, 1])
    test2 = Solution().findMaxConsecutiveOnes([1])
    print(test1)
    print(test2)
