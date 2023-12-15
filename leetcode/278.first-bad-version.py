#
# @lc app=leetcode id=278 lang=python3
#
# [278] First Bad Version
#

# @lc code=start
# The isBadVersion API is already defined for you.
# def isBadVersion(version: int) -> bool:
# def isBadVersion(n: int) -> bool:
#     if n == 3:
#         return True
#     return False


class Solution:
    def firstBadVersion(self, n: int) -> int:

        left, right = 0, n
        while left < right:
            mid = left + (right - left)//2
            if isBadVersion(mid):
                right = mid
            else:
                left = mid+1

        return left


# print(Solution().firstBadVersion(5))
# @lc code=end
