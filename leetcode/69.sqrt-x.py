#
# @lc app=leetcode id=69 lang=python3
#
# [69] Sqrt(x)
#

# @lc code=start 

class Solution:
    def mySqrt(self, x: int) -> int:
        left, right = 0, x

        while left <= right:
            mid = left + (right - left)//2
            if mid * mid <= x < (mid+1)*(mid+1):
                return mid
            elif mid * mid > x:
                right = mid - 1
            else:
                left = mid + 1
        return mid
print(Solution().mySqrt(8))
        # @lc code=end
