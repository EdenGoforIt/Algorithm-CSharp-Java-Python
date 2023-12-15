from typing import List


class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        max_profit = 0
        min = prices[0]
        for i in range(1, len(prices)):
            if prices[i] - min > max_profit:
                max_profit = prices[i] - min
            if prices[i] < min:
                min = prices[i]

        return max_profit


print(Solution().maxProfit([7, 1, 5, 3, 6, 4]))
