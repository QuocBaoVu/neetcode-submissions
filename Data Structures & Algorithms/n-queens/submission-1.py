class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        out = []
        col = set()
        diag = set()
        antiDiag = set()
        def backtrack(board, r):
            if r == n:
                out.append(board[:])
                return
            
            for c in range(n):
                # We are at row number row
                if (c in col) or (r-c in diag) or (r+c in antiDiag):
                    continue
                # make choice:
                col.add(c)
                diag.add(r-c)
                antiDiag.add(r+c)
                row = '.' * n
                row = row[:c] + 'Q' + row[c+1:]
                board.append(row)

                #backtrack
                backtrack(board, r+1)

                # unmake choice:
                col.remove(c)
                diag.remove(r-c)
                antiDiag.remove(r+c)
                board.pop()
        
        backtrack([], 0)
        return out