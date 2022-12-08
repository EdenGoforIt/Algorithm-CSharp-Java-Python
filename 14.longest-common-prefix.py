#
# @lc app=leetcode id=14 lang=python3
#
# [14] Longest Common Prefix
#
# @lc code=start
from typing import List


class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        # https://leetcode.com/problems/longest-common-prefix/solutions/127449/longest-common-prefix/
        # vertical scanning
        if strs is None:
            return ""
        if len(strs) == 1:
            return strs[0]

        word = strs[0]

        for i in range(len(word)):
            c = word[i]

            for w in strs[1:]:
                if i == len(w) - 1 or w[i] != c:
                    return word[:i]

        return ""

        # horizontal scanning
        # if strs is None:
        #     return ""

        # prefix = strs[0]
        # for i in range(1, len(strs)):
        #     while prefix not in strs[i]:
        #         prefix = prefix[0: len(prefix)-1]

        #         if not prefix:
        #             return ""
        # return prefix
print(Solution().longestCommonPrefix(["flower", "flower", "flower", "flower"]
                                     ))

# @lc code=end
