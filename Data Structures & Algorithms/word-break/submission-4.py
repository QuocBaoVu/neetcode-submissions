class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        word_dict = set(wordDict)
        n = len(s)
        dp = [False] * (n+1)
        dp[0] = True
        for right in range(1, n+1):
            for i in range(0, right):
                if dp[i] and s[i:right] in word_dict:
                    dp[right] = True
                    break
        return dp[n]
