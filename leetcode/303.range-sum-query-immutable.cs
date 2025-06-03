/*
 * @lc app=leetcode id=303 lang=csharp
 *
 * [303] Range Sum Query - Immutable
 */

// @lc code=start

public class NumArray
{
	private int[] sums;
	public NumArray(int[] nums)
	{
		sums = new int[nums.Length + 1];
		sums[0] = 0;

		for (var i = 0; i < nums.Length; i++)
		{
			sums[i + 1] = sums[i] + nums[i];
			Console.WriteLine($"sums[i]  ${sums[i + 1].ToString()}");
		}
	}

	public int SumRange(int left, int right)
	{
		return sums[right + 1] - sums[left];
	}
}

/**
 * Your NumArray object will be instantiated and called as such:
 * NumArray obj = new NumArray(nums);
 * int param_1 = obj.SumRange(left,right);
 */
// @lc code=end

