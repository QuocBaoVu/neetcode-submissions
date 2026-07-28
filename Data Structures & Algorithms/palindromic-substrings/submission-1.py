class Solution:
    def countSubstrings(self, s: str) -> int:

        def expand(s, left, right):
            c = 0
            while left>=0 and right < len(s) and s[left] == s[right]:
                left -= 1
                right += 1
                c += 1
            return c

        count = 0

        for i in range(len(s)):
            count += expand(s, i, i)
            count += expand(s, i, i+1)
        
        return count
        
