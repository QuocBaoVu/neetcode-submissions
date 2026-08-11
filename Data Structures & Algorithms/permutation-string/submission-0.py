class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s2) < len(s1):
            return False

        k = len(s1) # size of window

        s1_table = Counter(s1)

        window = defaultdict(int)
        left = 0
    
        for right in range(k-1):
            window[s2[right]] += 1

        for right in range(k-1, len(s2)):
            window[s2[right]] += 1
            
            if window == s1_table:
                return True
            
            window[s2[left]] -= 1
            if window[s2[left]] == 0:
                del window[s2[left]]
            left += 1

        return False


            

