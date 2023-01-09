from typing import List


class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:

        if len(strs) == 0:
            return ""
        current = strs[0]
        for i in range(1, len(strs)):
            temp = ""
            if len(current) == 0:
                break
            for j in range(len(strs[i])):
                if j < len(current) and current[j] == strs[i][j]:
                    temp += current[j]
                else:
                    break
            current = temp
        return current 

if __name__ == "__main__":
    list1 = ["flower", "flow", "flight"]
    list2 = ["dog", "racecar", "car"]
    print(Solution().longestCommonPrefix(list1))
    print(Solution().longestCommonPrefix(list2))
