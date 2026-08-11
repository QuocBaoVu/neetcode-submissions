class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if not s or not t or len(s) < len(t):
            return ""

        t_count = Counter(t)
        required = len(t_count)          # number of UNIQUE chars we need
        window_count = defaultdict(int)
        formed = 0                       # number of unique chars currently fully satisfied

        left = 0
        left_out, len_out = 0, float('inf')

        for right, c in enumerate(s):
            window_count[c] += 1
            if c in t_count and window_count[c] == t_count[c]:
                formed += 1             # this char just became "satisfied"

            while formed == required:
                if right - left + 1 < len_out:
                    left_out = left
                    len_out = right - left + 1

                lchar = s[left]
                window_count[lchar] -= 1
                if lchar in t_count and window_count[lchar] < t_count[lchar]:
                    formed -= 1          # this char just became "unsatisfied"
                left += 1

        return "" if len_out == float('inf') else s[left_out:left_out + len_out]