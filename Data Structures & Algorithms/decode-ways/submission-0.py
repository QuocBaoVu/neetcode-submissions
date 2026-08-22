class Solution:
    def numDecodings(self, s: str) -> int:
        def is_valid(s):
            if len(s) > 2:
                return False
            if len(s) == 2:
                if s[0] == '1':
                    return True
                elif s[0] == '2':
                    return s[1] in "0123456"
                else:
                    return False
            else:
                return s[0] != '0'
        
    
        # dp[i]: the number of way we can decode with string 0 -> i
        # way_before_i = dp[i-1]
        # out = None
        n = len(s)
        dp = [-1] * (n+1)
        dp[0] = 1

        for i in range(1, n+1):
            out = 0
            if is_valid(s[i-1:i]):
                out += dp[i-1]
            if i > 1:
                if is_valid(s[i-2:i]):
                    out += dp[i-2]
            dp[i] = out
        
        return dp[n]
            

        # if is_valid(s[i-1:i]) -> out = dp[i-1]
        #   if is_valid(s[i-2:i]) -> out = dp[i-2]
        #   dp[i] = out
        # else:
        #   dp[i]