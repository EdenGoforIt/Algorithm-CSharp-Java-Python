/*
 * @lc app=leetcode id=303 lang=csharp
 *
 * [303] Range Sum Query - Immutable
 */

// Input
//["NumArray","sumRange","sumRange","sumRange"]
//[[[-2,0,3,-5,2,-1]],[0,2],[2,5],[0,5]]

// @lc code=start
using System.Reflection.Emit;
using Internal;

public class NumArray
{
	private int[] sums;
	public NumArray(int[] nums)
	{
		sums = new int[nums.Length + 1];

		for (var i = 0; nums.Length; i++)
		{
			sums[i] = sums[i - 1] + sums[i];
			Console.WriteLine($"sums[i]", sums[i]);
		}
	}

	public int SumRange(int left, int right)
	{
		return sums[right] - sums[left];
	}
}

/**
 * Your NumArray object will be instantiated and called as such:
 * NumArray obj = new NumArray(nums);
 * int param_1 = obj.SumRange(left,right);
 */
// @lc code=end

