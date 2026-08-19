class Solution:
    def minimumEffortPath(self, heights: List[List[int]]) -> int:
        directions = [(0,1), (0,-1), (1, 0), (-1, 0)]
        X = len(heights)
        Y = len(heights[0])

        pq = [(0, (0,0))]

        effort = [[float('inf')] * Y for _ in range(X)]
        effort[0][0] = 0

        while pq:
            e, curr = heapq.heappop(pq)
            x, y = curr
            if e > effort[x][y]:
                continue

            for direction in directions:
                dx, dy = direction
                nx, ny = dx+x, dy+y

                if not (0<=nx<X and 0<=ny<Y):
                    continue
                de = abs(heights[nx][ny] - heights[x][y])
                ne = max(de, e)
                if ne < effort[nx][ny]:
                    effort[nx][ny] = ne
                    heapq.heappush(pq, (ne, (nx, ny)))
        
        return effort[X-1][Y-1]

