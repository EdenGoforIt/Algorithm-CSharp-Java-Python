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
            # -inf < -7 => buy1 = -7
            if buy1 < -price:
                buy1 = -price
                print(f"First buy on day {i} at price {price}")

            if sell1 < buy1 + price:
                sell1 = buy1 + price
                print(f"First sell on day {i} at price {price} → profit {sell1}")
            if buy2 < sell1 - price:
                buy2 = sell1 - price
                print(f"Second buy on day {i} at price {price} → profit {buy2}")
            if sell2 < buy2 + price:
                sell2 = buy2 + price
                print(f"Second sell on day {i} at price {price} → profit {sell2}")
        print(f"Max profit: {sell2}")
        return sell2


if __name__ == "__main__":

    Solution().maxProfit([7, 1, 5, 3])
# @lc code=end
