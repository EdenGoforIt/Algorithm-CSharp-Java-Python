#
# @lc app=leetcode id=88 lang=python3
#
# [88] Merge Sorted Array
#
from typing import List


# @lc code=start
class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        nums1[m:] = nums2[:n]
        nums1.sort()


# @lc code=end
