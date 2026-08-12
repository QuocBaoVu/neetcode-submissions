class Solution:
    def partition(self, s: str) -> List[List[str]]:
        out = []
        n = len(s)
        def backtrack(start, path):
            if start == len(s):
                out.append(path[:])

            for i in range(start+1, n+1):
                sub = s[start:i]
                check = dp[start][i-1]
                if check:
                    path.append(sub)
                    backtrack(i, path)
                    path.pop()
        
        dp = [[False] * n for _ in range(n)]

        for i in range(n):
            dp[i][i] = True

        for i in range(n):
            for j in range(i):
                if s[i] == s[j] and (i-j<=1 or dp[j+1][i-1]):
                    dp[j][i] = True
            
        backtrack(0, [])
        return out
