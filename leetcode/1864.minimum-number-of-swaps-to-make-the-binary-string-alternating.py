#
# @lc app=leetcode id=1864 lang=python3
#
# [1864] Minimum Number of Swaps to Make the Binary String Alternating
#

# @lc code=start
from collections import Counter


class Solution:
    def minSwaps(self, s: str) -> int:
        s = list(s)
        count = Counter(s)
        # Impossible to make it work
        if max(count['0'], count['1']) > min(count['0'], count['1']) + 1:
            return -1
        n = len(s)
        res = [0] * 2
        for i in range(0, n, 2):
            res[0] += s[i] == '0'
            res[1] += s[i] == '1'
        if count['0'] == count['1']:
            return min(res)
        # When there are one more 1, we have to replace 0's
        if count['0'] < count['1']:
            return res[0]
        else:
            return res[1]
        
        
        
        
        
        num = int(s)
        even = int(s[0])
        odd = 1 if even == 0 else 0
        even_not_matched = 0
        odd_not_matched = 0
        for i in range(len(s)):
            # even
            if i % 2 == 0 and int(s[i]) != even:
                even_not_matched += 1

            if i % 2 == 1 and int(s[i]) != odd:
                odd_not_matched += 1

        if even_not_matched == odd_not_matched:
            return even_not_matched
        # elif even_not_matched != odd_not_matched:
        #     return abs(even_not_matched - odd_not_matched)
        else:
            return -1


print(Solution().minSwaps("100"))
# @lc code=end
