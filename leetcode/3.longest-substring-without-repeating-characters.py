#
# @lc app=leetcode id=3 lang=python3
#
# [3] Longest Substring Without Repeating Characters
#

# @lc code=start
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        n = len(s)
        maxLength = 0
        charSet = set()
        left = 0
        
        for right in range(n):
            # abc, right 2 left 0 + 1
            if s[right] not in charSet:
                charSet.add(s[right])
                maxLength = max(maxLength, right - left + 1)
            # abcab, if a, b is in here, remove a, left = 2, 
            else:
                while s[right] in charSet:
                    charSet.remove(s[left])
                    left += 1
                charSet.add(s[right])
        
        return maxLength



# @lc code=end

print(Solution().lengthOfLongestSubstring('abcbbc'))
# print(Solution().lengthOfLongestSubstring('aaaa'))
# print(Solution().lengthOfLongestSubstring('pwwkew'))