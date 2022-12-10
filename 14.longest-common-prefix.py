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
        if strs is None:
            ""
        if len(strs) == 1:
            return strs[0]
        min_length = len(min(strs, key=len))

        low = 1
        high = min_length

        while low <= high:
            mid = (low+high)//2
            if self.isCommonPrefix(strs, mid):
                low = mid + 1
            else:
                high = mid - 1

        return strs[0][0: (low+high)//2]

    def isCommonPrefix(self, strs: List[str], mid: int) -> bool:
        candidate = strs[0][0: mid]

        for i in range(len(strs)):
            if not strs[i].startswith(candidate):
                return False

        return True
        # vertical scanning
        # if strs is None:
        #     return ""
        # if len(strs) == 1:
        #     return strs[0]

        # word = strs[0]

        # for i in range(len(word)):
        #     c = word[i]

        #     for w in strs[1:]:
        #         if i == len(w) - 1 or w[i] != c:
        #             return word[:i]

        # return ""

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
# print(Solution().longestCommonPrefix(["flower", "flow", "flaw"]))

# @lc code=end
