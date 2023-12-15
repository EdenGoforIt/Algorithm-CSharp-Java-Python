#
# @lc app=leetcode id=295 lang=python3
#
# [295] Find Median from Data Stream
#

# @lc code=start
import heapq


class MedianFinder:
    def __init__(self) -> None:
        self.small, self.large = [], []

    def addNum(self, num: int) -> None:
        heapq.heappush(self.small, -1 * num)
        # https://www.geeksforgeeks.org/heap-queue-or-heapq-in-python/
        # heap is for the max heap means -> 1,2,3,4
        # every number in small should be smaller than the numbers in the large
        # largest value from the small heap and large heap
        # 5 < 3 then move 5 to the large heap to the right
        if self.small and self.large and (-1 * self.small[0]) > self.large[0]:
            val = -1 * heapq.heappop(self.small)
            heapq.heappush(self.large, val)

        # when the small has more numbers than the large more than 2
        # [-2, -1] > [] -> [-1] - [2]
        if len(self.small) > len(self.large) + 1:
            val = -1 * heapq.heappop(self.small)
            heapq.heappush(self.large, val)
        # [-2, -1] > [3,4,5,6] -> [-2, -1]
        if len(self.large) > len(self.small) + 1:
            val = heapq.heappop(self.large)
            heapq.heappush(self.small, -1 * val)

    def findMedian(self) -> float:
        if len(self.small) > len(self.large):
            return -1 * self.small[0]
        if len(self.large) > len(self.small):
            return self.large[0]

        return ((-1 * self.small[0]) + self.large[0]) / 2


# Your MedianFinder object will be instantiated and called as such:
# obj = MedianFinder()
# obj.addNum(num)
# param_2 = obj.findMedian()
# @lc code=end
