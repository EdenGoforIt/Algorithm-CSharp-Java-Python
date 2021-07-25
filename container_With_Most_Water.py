import datetime
from typing import List


class Solution:
    def maxArea(self, height: List[int]) -> int:
        maxarea = 0
        head = 0
        tail = len(height) - 1
        while (head < tail):
            min_value = min(height[head], height[tail])
            diff = tail - head
            maxarea = max(maxarea, min_value * diff)
            if height[head] < height[tail]:
                head += 1
            else:
                tail -= 1

        return maxarea


if __name__ == '__main__':
    start_time = datetime.datetime.now()

    nums = [1, 8, 6, 2, 5, 4, 8, 3, 7]
    nums2 = [1, 2, 1]
    nums3 = [4, 3, 2, 1, 4]
    nums4 = [1, 8, 6, 2, 5, 4, 8, 3, 7]
    test = Solution().maxArea(nums4)
    print(test)

    end_time = datetime.datetime.now()
    diff = int((end_time - start_time).total_seconds()*1000)
    print("Execution time: {} ".format(diff))
