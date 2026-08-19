class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        X = len(grid)
        Y = len(grid[0])
        directions = [(0,1), (0,-1), (1, 0), (-1, 0)]
        def dfs(node, grid):
            stack = deque([node])
            area = 1
            x, y = node
            grid[x][y] = 2
            
            while stack:
                curr = stack.pop()
                x, y = curr

                for d in directions:
                    dx, dy = d
                    nx, ny = x+dx, y+dy
                    if (0<=nx<X and 0<=ny<Y) and grid[nx][ny] == 1:
                        area += 1
                        grid[nx][ny] = 2
                        stack.append((nx,ny))
            return area
                    

        out = 0

        for i in range(X):
            for j in range(Y):
                if grid[i][j] == 1:
                    area = dfs((i, j), grid)
                    out = max(out, area)

        return out

