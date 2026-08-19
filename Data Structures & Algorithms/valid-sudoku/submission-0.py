class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        rows = defaultdict(set)
        cols = defaultdict(set)
        boxs = [[set() for _ in range(3)] for _ in range(3)]

        for i in range(9):
            for j in range(9):
                v = board[i][j]
                if v == ".":
                    continue
                r = i
                c = j
                bi = r//3
                bj = c//3

                if v in rows[r] or v in cols[c] or v in boxs[bi][bj]:
                    return False
                rows[r].add(v)
                cols[c].add(v)
                boxs[bi][bj].add(v)
        
        return True