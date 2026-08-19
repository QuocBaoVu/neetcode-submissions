class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        X = len(grid)
        Y = len(grid[0])
        directions = [(0,1), (0,-1), (1, 0), (-1, 0)]
        queue = deque()
        

        for i in range(X):
            for j in range(Y):
                if grid[i][j] == 0:
                    queue.append((0,(i,j)))

        while queue:
            cost, curr = queue.popleft()
            x, y = curr
            for d in directions:
                dx, dy = d
                nx, ny = x+dx, y+dy
                ncost = cost+1
                if (0<=nx<X and 0<=ny<Y) and grid[nx][ny] != 0 and grid[nx][ny] != -1:
                    if ncost >= grid[nx][ny]:
                        continue
                    grid[nx][ny] = ncost
                    queue.append((ncost, (nx, ny)))
