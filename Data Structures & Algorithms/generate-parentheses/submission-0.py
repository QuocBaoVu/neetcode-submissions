class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        out = []

        def backtrack(path, op, cl):
            if len(path) == n * 2:
                out.append(path[:])
            
            if op < n:
                path += '('
                backtrack(path, op+1, cl)
                path = path[:-1]
            if cl < op:
                path += ')'
                backtrack(path, op, cl+1)
                path = path[:-1]
        
        backtrack('', 0, 0)
        return out
