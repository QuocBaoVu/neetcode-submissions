class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        sorted_strs = [''.join(sorted(s)) for s in strs]
        table = defaultdict(list)

        for i in range(len(strs)):
            s = sorted_strs[i]
            table[s].append(strs[i])
        
        out = []
        for val in table.values():
            out.append(val)
        return out