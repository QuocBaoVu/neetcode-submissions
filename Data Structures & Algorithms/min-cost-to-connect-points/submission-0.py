class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        visited = [False] * len(points)
        if not points:
            return 0
        out = 0
        pq = []
        heapq.heappush(pq, (0, 0))

        while pq:
            dist, curr = heapq.heappop(pq)
            if visited[curr]:
                continue
            out += dist
            visited[curr] = True
            point = points[curr]
            for i in range(len(points)):
                if visited[i]:
                    continue
                new_point = points[i]
                new_dist = abs(new_point[0] - point[0]) + abs(new_point[1] - point[1])
                heapq.heappush(pq, (new_dist, i))
        return out


