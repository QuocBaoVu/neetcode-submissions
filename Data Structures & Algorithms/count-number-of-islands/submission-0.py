class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        m = len(grid)
        n = len(grid[0])
        visited = [[0] * n for _ in range(m)]
        def dfs(x,y):
            if grid[x][y] == "1":
                visited[x][y] = 1
                dirs = [(+1,0), (-1,0), (0,+1), (0,-1)]

                for d in dirs:
                    dx, dy = d
                    nx = x+dx
                    ny = y+dy
                    if 0 <= nx < m and 0 <= ny < n:
                        if visited[nx][ny] == 1:
                            continue
                        dfs(nx, ny)
                
            return
        
        count = 0
        for i in range(m):
            for j in range(n):
                if grid[i][j] == "0":
                    continue
                if visited[i][j] == 1:
                    continue
                dfs(i, j)
                count += 1
        return count
                
                    
