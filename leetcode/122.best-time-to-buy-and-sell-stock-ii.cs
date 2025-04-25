/*
 * @lc app=leetcode id=122 lang=csharp
 *
 * [122] Best Time to Buy and Sell Stock II
 */

// @lc code=start
public class Solution
{
	public int MaxProfit(int[] prices)
	{
		int maxProfit = 0;
		for (int i = 1; i < prices.Length; i++)
		{
			Console.WriteLine($"prices[{i}] = {prices[i]}");

			if (prices[i] > prices[i - 1])
			{
				maxProfit += prices[i] - prices[i - 1];
			}
		}

		return maxProfit;
	}
}
// @lc code=end

