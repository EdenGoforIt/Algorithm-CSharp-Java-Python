#
# @lc app=leetcode id=67 lang=python3
#
# [67] Add Binary
#

# @lc code=start
class Solution:
    def addBinary(self, a: str, b: str) -> str:
        max_length = len(a) if len(a) > len(b) else len(b)
        a = a.zfill(max_length)
        b = b.zfill(max_length)

        result = ''
        carry_over = 0
        for i in range(max_length - 1, -1, -1): 
            sum = int(a[i])+int(b[i])+carry_over

            if sum > 1:
                result += str((sum) % 2)
                carry_over = 1

            else:
                result += str(sum)
                carry_over = 0

        if carry_over > 0:
            result += str(carry_over)

        return result[::-1]


print(Solution().addBinary("1111", "1111"))
# @lc code=end
