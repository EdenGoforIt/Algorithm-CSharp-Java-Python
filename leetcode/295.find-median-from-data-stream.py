#
# @lc app=leetcode id=295 lang=python3
#
# [295] Find Median from Data Stream
#
import heapq


# @lc code=start
class MedianFinder:

    def __init__(self):
        # max heap
        # the value of any parent node is always greater than or equal to the value of its child nodes.
        self.small = []
        # min heap
        #      10
        #     /   \
        #   20     30
        #  /  \    /  \
        # 40  50  60  70
        self.large = []

    def addNum(self, num: int) -> None:
        # heapq only supports min heap
        # if max heap is empty or num is less than or equal to the largest number in max heap
        if not self.small or num <= -self.small[0]:
            # we are saving negative values to simulate max heap here.
            #      -10
            #     /    \
            #   -20    -30
            #  /   \   /   \
            # -40  -50 -60  -70
            heapq.heappush(self.small, -num)
        else:
            heapq.heappush(self.large, num)

        # Balance the heaps
        # if max heap has more number then add it to min heap
        # we are trying to save if odd number, max heap will have more number
        # 1,2 min heap and 3,4,5 max heap (small)
        if len(self.small) > len(self.large) + 1:
            heapq.heappush(self.large, -heapq.heappop(self.small))
        elif len(self.large) > len(self.small):
            heapq.heappush(self.small, -heapq.heappop(self.large))

    def findMedian(self) -> float:
        # so that if max heap has more we return mean it's. odd number
        # and max heap has more number.
        if len(self.small) > len(self.large):
            return -self.small[0]
        return (-self.small[0] + self.large[0]) / 2


# Your MedianFinder object will be instantiated and called as such:
# obj = MedianFinder()
# obj.addNum(num)
# param_2 = obj.findMedian()
# @lc code=end
