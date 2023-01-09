from typing import List


class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        result = []
        length = len(nums)
        for left in range(length - 2):
            # avoid duplication
            if left > 0 and nums[left] == nums[left-1]:
                continue
            mid = left + 1
            right = length - 1
            while mid < right:
                sum = nums[left] + nums[mid] + nums[right]
                if sum < 0:
                    mid += 1
                elif sum > 0:
                    right -= 1
                else:
                    result.append([nums[left], nums[mid], nums[right]])
                    while mid < right and nums[mid] == nums[mid+1]:
                        mid += 1
                    while mid < right and nums[right] == nums[right - 1]:
                        right -= 1
                    mid += 1
                    right -= 1
        return result


if __name__ == '__main__':
    test1 = Solution().threeSum([-2, 0, 0, 2, 2])
    print(test1)
