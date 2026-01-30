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
        for i, price in enumerate(prices):
            # We start by making a debt of the price as we are buying the stock
            # with max we compare which is better to buy at the cheaper price
            buy1 = max(buy1, -price)
            sell1 = max(sell1, buy1 + price)
            buy2 = max(buy2, sell1 - price)
            sell2 = max(sell2, buy2 + price)

        print(f"Max profit: {sell2}")
        return sell2


if __name__ == "__main__":

    Solution().maxProfit([7, 1, 5, 3])
# @lc code=end
