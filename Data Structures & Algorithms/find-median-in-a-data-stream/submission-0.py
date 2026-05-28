import heapq

class MedianFinder:

    def __init__(self):
        # max-heap to store the smaller half of numbers (inverted values)
        self.small = []
        # min-heap to store the larger half of numbers
        self.large = []

    def addNum(self, num: int) -> None:
        # 1. Push to max-heap first (simulated with negative numbers)
        heapq.heappush(self.small, -num)
        
        # 2. Make sure every element in small is <= every element in large
        if self.small and self.large and (-self.small[0] > self.large[0]):
            val = -heapq.heappop(self.small)
            heapq.heappush(self.large, val)
            
        # 3. Handle size balancing: heaps shouldn't differ in size by more than 1
        if len(self.small) > len(self.large) + 1:
            val = -heapq.heappop(self.small)
            heapq.heappush(self.large, val)
        elif len(self.large) > len(self.small) + 1:
            val = heapq.heappop(self.large)
            heapq.heappush(self.small, -val)

    def findMedian(self) -> float:
        # If one half has more elements, its top element is the exact median
        if len(self.small) > len(self.large):
            return float(-self.small[0])
        if len(self.large) > len(self.small):
            return float(self.large[0])
            
        # If even, the median is the average of both tops
        return (-self.small[0] + self.large[0]) / 2.0