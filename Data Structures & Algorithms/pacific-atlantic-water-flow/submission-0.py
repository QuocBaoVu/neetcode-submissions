class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        directions=[(0,1), (1,0), (-1,0), (0,-1)]
        X = len(heights)
        Y = len(heights[0])

        def dfs(node, visited):
            x, y = node
            stack = deque([node])
            visited[x][y] = True

            while stack:
                curr = stack.pop()
                x, y = curr
                for direction in directions:
                    dx, dy = direction
                    nx, ny = x+dx, y+dy
                    if not (0<=nx<X and 0<=ny<Y) or visited[nx][ny] or heights[nx][ny] <heights[x][y]:
                        continue
                    stack.append((nx, ny))
                    visited[nx][ny]=True
        
        P_visited = [[False] * Y for _ in range(X)]
        A_visited = [[False] * Y for _ in range(X)]
        
        for i in range(X):
            for j in range(Y):
                if i == 0 or j == 0:
                    if not P_visited[i][j]:
                        dfs((i,j), P_visited)

                if i == X-1 or j == Y-1:
                    if not A_visited[i][j]:
                        dfs((i,j), A_visited)

        out = []
        for i in range(X):
            for j in range(Y):
                    if P_visited[i][j] and A_visited[i][j]:
                        out.append([i,j])
        return out