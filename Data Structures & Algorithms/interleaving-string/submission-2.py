class Solution:
    def isInterleave(self, s1: str, s2: str, s3: str) -> bool:
        # brute force
        if len(s1) + len(s2) != len(s3):
            return False
        memo = defaultdict()
        def solve(i,j,k):
            if (i,j,k) in memo:
                return memo[(i,j,k)]
        
            if k >= len(s3):
                return True
            out = False
            if i < len(s1):
                if s1[i] == s3[k]:
                    out = out or solve(i+1,j,k+1)
            if j < len(s2):
                if s2[j] == s3[k]:
                    out = out or solve(i, j+1, k+1)
            memo[(i,j,k)] = out
            return out
        return solve(0,0,0)