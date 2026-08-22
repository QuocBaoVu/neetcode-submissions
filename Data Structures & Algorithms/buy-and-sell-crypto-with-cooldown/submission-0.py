class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        n = len(prices)

        # dp = [0] * n #dp[i]: max profit at point i 
        # dp[0] = 0

        # if n > 1:
        #     dp[1]=max(nums[1] - nums[0], 0)
        # if n > 2:
        #     dp[2]=max(nums[2] - nums[0], nums[2] - nums[1], 0)

        # for i in range(3, n):
        #     dp[i] = max()

        memo = {}
        memo[(0,False)] = 0
        memo[(0, True)] = - prices[0]

        # max profit at point i, such that in the end of the day, status is own_stock
        for i in range(1, n):

            # Case 1: result = True
            # already own from prev step -> keep
            keep = memo[(i-1,True)]
            # not own -> buy
            # do selling check:
            if i < 2:
                buy = memo[(i-1,False)] - prices[i]
            else:
                buy = memo[(i-2,False)] - prices[i]


            memo[(i,True)] = max(keep, buy)
            
            # Case 2: result = False
            # already own -> sell -> go to i+2 
            sell = memo[(i-1,True)] + prices[i]
            # not own -> skip
            skip = memo[(i-1,False)]
            if sell >= skip:
                memo[(i,False)] = sell
            else:
                memo[(i,False)] = skip
        
        return max(memo[(n-1, True)], memo[(n-1), False])