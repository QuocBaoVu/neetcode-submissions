class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        def dist(p1, p2):
            x1, y1 = p1
            x2, y2 = p2

            return math.sqrt((x1 - x2)**2 + (y1 - y2)**2)
        origin = [0,0]
        points_with_dist = [[-dist(p, origin), p] for p in points]

        heap = []

        for p in points_with_dist:
            heapq.heappush(heap, p)
            if len(heap) > k:
                heapq.heappop(heap)
        
        out = [p[1] for p in heap]
        return out