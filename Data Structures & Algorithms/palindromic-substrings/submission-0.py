class Solution:
    def countSubstrings(self, s: str) -> int:
        # we can dp this: 
        # dp[j:i] = dp[j+1:i-1] and s[i] == s[j]
        # i = j -> True
        # i - j == 1 -> s[i] == s[j]
        n = len(s)
        dp = [[False] * n for _ in range(n)]
        count = 0
        for i in range(n):
            dp[i][i] = True
            for j in range(0, i):
                if i - j == 1:
                    dp[j][i] = s[j] == s[i]
                else:
                    dp[j][i] = dp[j+1][i-1] and (s[j] == s[i])

        for i in range(n):
            for j in range(n):
                if dp[i][j]:
                    count += 1
        return count
        

        