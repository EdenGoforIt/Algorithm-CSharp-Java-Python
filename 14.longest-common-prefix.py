#
# @lc app=leetcode id=14 lang=python3
#
# [14] Longest Common Prefix
#
# @lc code=start
from typing import List


class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:

        # vertical scanning


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


print(Solution().longestCommonPrefix(["flower", "flow", "flight"]))

# @lc code=end
