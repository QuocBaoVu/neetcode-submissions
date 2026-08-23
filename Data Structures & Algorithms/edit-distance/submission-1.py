class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        
        # queue = deque()
        # queue.append(word1)
        # edit = 0
        # memo = {} #kinda like a visited
        # memo[word1] = 0
        # while queue:
        #     edit += 1
        #     n = len(queue)
        #     for _ in range(n):
        #         curr = queue.popleft()
        #         if curr == word2:
        #             return edit
        #         if curr in memo:
        #             continue
        #         # insert: then append to queue
        #         # delete: then append to queue
        #         # replace: then append to queue

        # Step 1: State: dp[i][j] = number of operation to change word1[:i] to word2[:j]

        # Step 2: Recursion: 

        # Base case:
        n = len(word1)
        m = len(word2)
        dp = [[0] * (m+1) for _ in range(n+1)]

        for i in range(n+1):
            dp[i][0] = i
        for i in range(m+1):
            dp[0][i] = i
        
        for i in range(1, n+1):
            for j in range(1, m+1):
                if word1[i-1] == word2[j-1]:
                    dp[i][j] = dp[i-1][j-1]
                else:
                    dp[i][j] = min(
                        dp[i-1][j-1] + 1,
                        dp[i][j-1] + 1,
                        dp[i-1][j] + 1
                    )
        return dp[n][m]
        


