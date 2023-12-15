

from typing import List


class Solution:
    def wordBreak(self, s: str, words: List[str]) -> bool:
        #
        # loop
        #text = slice (index)
        # if there is, then slice from the string
        # continue until the end
        # if there is anything left false otherwise true

        ok = [True]
        for i in range(1, len(s)+1):
            ok += any(ok[j] and s[j:i] in words for j in range(i)),
         
        return ok[-1]

    # left_over = s
    # word = ''
    # for i in range(len(s)):
    #     word += s[i]
    #     if word in wordDict:
    #         left_over = s[i+1:]
    #         word = ''

    # # check if there is anything left in left_word
    # return False if len(left_over) > 0 else True


if __name__ == '__main__':

    result = Solution().wordBreak("leetcode", ["leet", "code"])
    print(result == True)
    # result = Solution().wordBreak("aaaaaaa", ["aaaa", "aaa"])
    # print(result == True)
    # result = Solution().wordBreak("applepenapple", ["apple", "pen"])
    # print(result == True)
