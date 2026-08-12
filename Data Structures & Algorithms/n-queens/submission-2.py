class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        out = []
        col = set()
        diag = set()
        antiDiag = set()
        board = [["." for _ in range(n)] for _ in range(n)]
        def backtrack(board, r):
            if r == n:
                out.append(["".join(i) for i in board])
                return
            
            for c in range(n):
                # We are at row number row
                if (c in col) or (r-c in diag) or (r+c in antiDiag):
                    continue
                # make choice:
                col.add(c)
                diag.add(r-c)
                antiDiag.add(r+c)
                board[r][c] = 'Q'

                #backtrack
                backtrack(board, r+1)

                # unmake choice:
                col.remove(c)
                diag.remove(r-c)
                antiDiag.remove(r+c)
                board[r][c] = '.'
        
        backtrack(board, 0)
        return out