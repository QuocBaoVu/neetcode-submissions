class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        rotten = []
        X = len(grid)
        Y = len(grid[0])

        fresh = 0
        for i in range(X):
            for j in range(Y):
                if grid[i][j] == 2:
                    # Rotten:
                    rotten.append((i,j))
                if grid[i][j] == 1:
                    fresh += 1

        queue = deque(rotten)

        directions = [(0,1), (1,0), (-1,0), (0,-1)]
        time = 0

        while queue and fresh>0:
            time += 1
            n = len(queue)
            for _ in range(n):
                curr = queue.popleft()
                x, y = curr
                for direction in directions:
                    dx, dy = direction
                    nx, ny = x+dx, y+dy
                    if not (0<=nx<X and 0<=ny<Y) or grid[nx][ny] != 1:
                        continue
                    grid[nx][ny] = 2
                    queue.append((nx, ny))
                    fresh -= 1


        return time if fresh == 0 else -1
            

