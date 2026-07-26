class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        # all the move need (m-1) down and (n-1) right, we can mix in what ever 
        # order we want 

        # math is: mC(m+n) = (m+n)! / m!n!

        m = m - 1
        n = n - 1
        return math.comb(m + n, m)