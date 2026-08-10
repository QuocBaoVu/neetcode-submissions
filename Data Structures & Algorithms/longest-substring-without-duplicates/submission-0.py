class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        freq = defaultdict(int)

        left = 0
        out = 0

        for right in range(len(s)):
            c = s[right]
            freq[c] += 1

            while right - left + 1 > len(freq):
                freq[s[left]] -= 1
                if freq[s[left]] == 0:
                    del freq[s[left]]
                left += 1

            out = max(out, right - left + 1)

        return out

