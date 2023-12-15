#
# @lc app=leetcode id=953 lang=python3
#
# [953] Verifying an Alien Dictionary
#

# @lc code=start

from typing import List


class Solution:
    def isAlienSorted(self, words: List[str], order: str) -> bool:
        # for index, something in enumerate(order)
        ind = {c: i for i, c in enumerate(order)}
        test = {c: i for i, c in enumerate(["One", "Two"])}
        print(test)
        words = [[ind[c] for c in w] for w in words] 
        return all(w1 <= w2 for w1, w2 in zip(words, words[1:]))


print(Solution().isAlienSorted(
    ["hello", "leetcode"], "hlabcdefgijkmnopqrstuvwxyz"))
# @lc code=end
