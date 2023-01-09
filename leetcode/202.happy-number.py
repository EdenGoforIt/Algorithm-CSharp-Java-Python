#
# @lc app=leetcode id=202 lang=python3
#
# [202] Happy Number
#

# @lc code=start
from numpy import true_divide


class Solution:
    def isHappy(self, n: int) -> bool:
        visited = set()

        while n not in visited:
            visited.add(n)
            n = self.sumOfSquare(n)

            if n == 1:
                return True

        return False

    def sumOfSquare(self, n: int) -> int:
        output = 0

        while n:
            digit = n % 10  # 1
            digit = digit ** 2  # 1
            output += digit  # 81 + 1
            n = n//10  # 0

        return output  # 81 +1


print(Solution().isHappy(19))
# @lc code=end
