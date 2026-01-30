#
# @lc app=leetcode id=46 lang=python3
#
# [46] Permutations
#
from typing import List


# @lc code=start
class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        if len(nums) == 0:
            return [[]]
        answer = []
        for i, current in enumerate(nums):
            # with [1,2,3], this will return [2,3]
            remaining = nums[:i] + nums[i + 1 :]
            # here we look [2,3]
            # if 2, then
            for p in self.permute(remaining):
                # with [2,3], this will return [[2,3], [3,2]]
                answer.append([current] + p)
        print(answer)
        return answer


if __name__ == "__main__":
    # Example test case
    Solution().permute([1, 2, 3])
