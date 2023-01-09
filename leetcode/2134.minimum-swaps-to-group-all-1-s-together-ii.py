#
# @lc app=leetcode id=2134 lang=python3
#
# [2134] Minimum Swaps to Group All 1's Together II
#
from typing import List

# @lc code=start


class Solution:
    def minSwaps(self, nums: List[int]) -> int:
        # get the total of 1's in the list
        # this will be the window size
        window_size = nums.count(1)

        # get the first window size and calculate zeros
        # the number of zeros will be the number of minimum swap is required
        min_swap = current_zeros = nums[:window_size].count(0)
        nums = nums + nums[:window_size - 1]

        for end_index in range(window_size, len(nums)):
            current_zeros -= 1 if nums[end_index - window_size] == 0 else 0

            current_zeros += 1 if nums[end_index] == 0 else 0

            min_swap = min(current_zeros, min_swap)

        return min_swap


print(Solution().minSwaps([1, 1, 0, 0, 1]))

# print(Solution().minSwaps([1, 0, 0, 1]))
# print(Solution().minSwaps([1, 0, 1]))
# print(Solution().minSwaps([1, 0, 1, 0]))
# print(Solution().minSwaps([1, 0, 0, 1]))
# print(Solution().minSwaps([1, 0, 0, 0, 1]))

# @lc code=end
