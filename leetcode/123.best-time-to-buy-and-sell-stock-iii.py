#
# @lc app=leetcode id=123 lang=python3
#
# [123] Best Time to Buy and Sell Stock III
#
from typing import List


# @lc code=start
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        buy1, buy2 = float("-inf"), float("-inf")
        sell1, sell2 = 0, 0
        # [7, 1, 5, 3]
        for price, i in enumerate(prices):
            # We start by making a debt of the price as we are buying the stock
            # with max we compare which is better to buy at the cheaper price
            buy1 = max(buy1, -price)
            

        
        print(f"Max profit: {sell2}")
        return sell2


if __name__ == "__main__":

    Solution().maxProfit([7, 1, 5, 3])
# @lc code=end
