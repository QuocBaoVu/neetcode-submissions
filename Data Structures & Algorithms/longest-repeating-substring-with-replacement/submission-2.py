class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        window = defaultdict(int)

        left = 0
        out = 1
        for right in range(len(s)):
            window[s[right]] += 1
            while right - left + 1 - max(window.values()) > k:
                window[s[left]] -= 1
                left += 1
            out = max(out, right - left + 1)

        return out