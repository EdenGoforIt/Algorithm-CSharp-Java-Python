import heapq


class MedianFinder:
    def __init__(self) -> None:
        self.small, self, large = [], []

    def addNum(self, num: int) -> None:
        heapq.heappush(self.small, -1 * num)
        # https://www.geeksforgeeks.org/heap-queue-or-heapq-in-python/
        # heap is for the max heap means -> 1,2,3,4
        # every number in small should be smaller than the numbers in the large
        if self.small and self.large and (-1 * self.small[0]) > self.large[0]:
            val = -1 * heapq.heappop(self.small)
            heapq.heappush(self.large, val)

        # when the small has more numbers then the large more than 2
        if len(self.small) > len(self.large) + 1:
            val = -1 * heapq.heappop(self.small)
            heapq.heappush(self.large, val)
        # 1,2 > 3,4,5
        if len(self.large) > len(self.small) + 1:
            val = heapq.heappop(self.large)
            heapq.heappush(-1 * val)

    def findMedian(self) -> float:
        if len(self.small) > len(self.large):
            return -1 * self.small[0]
        if len(self.large) > len(self.small):
            return self.large[0]

        return ((-1 * self.small[0]) + self.large[0]) / 2
