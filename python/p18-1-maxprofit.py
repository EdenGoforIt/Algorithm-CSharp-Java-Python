from typing import List


def find_max_profit_brute_force(prices: List[str]) -> int:
    min = prices[0]
    max_profit = 0
    for i in range(1, len(prices)):
        profit = prices[i] - min
        if profit > max_profit:
            max_profit = profit
        if prices[i] < min:
            min = prices[i]

    return max_profit

    # max_profit = 0

    # for i in range(0, len(prices)-1):
    #     for j in range(i+1, len(prices)):
    #         profit = prices[j] - prices[i]
    #         if profit > max_profit:
    #             max_profit = profit

    # return max_profit
stock = [10300, 9600, 9800, 8200, 7800, 8300, 9500, 9800, 10200, 9500]

print(find_max_profit_brute_force(stock))
