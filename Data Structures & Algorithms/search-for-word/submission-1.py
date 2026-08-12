class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        out = False
        n = len(word)
        X = len(board)
        Y = len(board[0])
        directions = [(+1,0), (-1,0), (0, +1), (0,-1)]
        visited = [[False] * Y for _ in range(X)]

        def backtrack(pos, nxt, visited):
            nonlocal out
            x, y = pos
            if board[x][y] != word[nxt] or visited[x][y]:
                return
            visited[x][y] = True
            nxt += 1
            if nxt == n:
                out = True
                return
            for direction in directions:
                dx, dy = direction
                nx = x + dx
                ny = y + dy
                if not (0 <= nx < X) or not (0 <= ny < Y):
                    continue
                npos = (nx, ny)
                backtrack(npos, nxt, visited)
            visited[x][y] = False
        
        for i in range(X):
            for j in range(Y):
                if out == True:
                    return True
                backtrack((i, j), 0, visited)
            
        return out
                