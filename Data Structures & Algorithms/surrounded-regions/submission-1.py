class Solution:
    def solve(self, board: List[List[str]]) -> None:
        X = len(board)
        Y = len(board[0])
        directions = [(0,1), (0,-1), (1, 0), (-1, 0)]
        visited = [[0] * Y for _ in range(X)]

        def dfs(node):
            stack = deque([node])
            x, y = node
            visited[x][y] = 1
            
            while stack:
                curr = stack.pop()
                x, y = curr

                for d in directions:
                    dx, dy = d
                    nx, ny = x+dx, y+dy
                    if (0<=nx<X and 0<=ny<Y) and board[nx][ny] == "O" and not visited[nx][ny]:
                        visited[nx][ny] = 1
                        stack.append((nx,ny))
        
        for i in range(X):
            for j in range(Y):
                if board[i][j] == "O":
                    if i == 0 or i == X-1 or j == 0 or j == Y-1:
                        dfs((i,j))

        for i in range(X):
            for j in range(Y):
                if board[i][j] == "O" and visited[i][j] == 0:
                    board[i][j] = "X"
    