#
# @lc app=leetcode id=13 lang=python3
#
# [13] Roman to Integer
#

# @lc code=start
class Solution:
    def romanToInt(self, s: str) -> int:
        romans = {
            'I': 1,
            'IV': 4,
            'V': 5,
            'IX': 9,
            'X': 10,
            'XL': 40,
            'L': 50,
            'XC': 90,
            'C': 100,
            'CD': 400,
            'D': 500,
            'CM': 900,
            'M': 1000
        }

        # save the last to remove index out of range error
        ans = romans[s[len(s)-1]]

        for i in range(len(s)-2, -1, -1):
            if romans[s[i]] < romans[s[i+1]]:
                ans -= romans[s[i]]
            else:
                ans += romans[s[i]]
        return ans


# print(Solution().romanToInt("III"))

# @lc code=end
