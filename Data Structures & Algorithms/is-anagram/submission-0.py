class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        c_s = Counter(s)
        c_t = Counter(t)

        if c_s != c_t:
            return False
        return True