class MedianFinder:

    def __init__(self):
        self.arr = []

    def addNum(self, num: int) -> None:
        self.arr.append(num)
        self.arr.sort()

    def findMedian(self) -> float:
        n = len(self.arr)
        if n % 2 == 0:
            med = n // 2
            median = (self.arr[med] + self.arr[med-1]) / 2
        else:
            med = n // 2
            median = self.arr[med]
        
        return median