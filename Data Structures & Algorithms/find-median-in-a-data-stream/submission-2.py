class MedianFinder:

    def __init__(self):
        self.left = [] # max_heap
        self.right = [] # min_heap
        # We try to keep the len of these 2 heap +-1 of each other
    def addNum(self, num: int) -> None:
        if len(self.right) == 0:
            heapq.heappush(self.right, num)
            return
        if num > self.right[0]:
            heapq.heappush(self.right, num)
        else:
            heapq.heappush(self.left, -num)
        if len(self.right) - len(self.left) >= 2:
            heapq.heappush(self.left, -heapq.heappop(self.right))
        elif len(self.left) - len(self.right) >= 2:
            heapq.heappush(self.right, -heapq.heappop(self.left))
        return

    def findMedian(self) -> float:
        l = len(self.left)
        r = len(self.right)
        if l > r: 
            return - self.left[0]
        if r > l:
            return self.right[0]
        else:
            return (-self.left[0] + self.right[0]) / 2