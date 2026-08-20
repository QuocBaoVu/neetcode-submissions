class Solution:
    def climbStairs(self, n: int) -> int:
        state = {}

        state[1] = 1
        state[0] = 1

        def memo(n):
            if n in state: 
                return state[n]
            this = memo(n-1) + memo(n-2)   
            state[n] = this
            return this
        
        return memo(n)