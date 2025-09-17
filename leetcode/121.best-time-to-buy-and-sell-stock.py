#
# @lc app=leetcode id=121 lang=python3
#
# [121] Best Time to Buy and Sell Stock
#
from typing import List


# @lc code=start
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        max_profiit = 0
        for i in range(1, len(prices)):
            if prices[i - 1] < prices[i]:
                max_profiit += prices[i] - prices[i - 1]

        return max_profiit


# @lc code=end
