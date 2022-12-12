
from typing import List


def binary_search(nums: List[int], target: int) -> int:
    start = 0
    end = len(nums) - 1

    while start <= end:
        mid = (start + end)//2
        if target == nums[mid]:
            return mid

        elif target > nums[mid]:
            start = mid + 1
        else:
            end = mid - 1

    return -1


print(binary_search([1, 2, 3, 4, 5, 6], 2))
