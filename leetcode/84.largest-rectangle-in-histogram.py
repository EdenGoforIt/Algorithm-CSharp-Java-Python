#
# @lc app=leetcode id=84 lang=python3
#
# [84] Largest Rectangle in Histogram
#

# @lc code=start
from typing import List

# https://gist.github.com/jacksongabbard/9cc21485c5e02d145203fa28651f42c4


class Solution:

    def largestRectangleArea(self, heights: List[int]) -> int:
        heights.append(0)  # add zero on the end
        # initialize by -1. This is a reference to the zero that we have added
        stack = [-1]
        ans = 0
        for i in range(len(heights)):
            # -1 will be the last element in the list, so we are starting from zero
            while heights[i] < heights[stack[-1]]: # if descending order like 3,2
                h = heights[stack.pop()]
                w = (i - stack[-1])-1
                ans = max(ans, h * w)
            stack.append(i)
        heights.pop()
        return ans

        # @lc code=end


Solution().largestRectangleArea([2, 1, 4, 3])
