class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        out = []
        n = len(candidates)
        candidates.sort()

        def backtrack(start, path, target):
            if target == 0:
                out.append(path[:])
                return
            for i in range(start, n):
                if candidates[i] > target:
                    break
                if i > start and candidates[i] == candidates[i-1]:
                    continue
                path.append(candidates[i])
                backtrack(i+1, path, target-candidates[i])
                path.pop()
        
        backtrack(0, [], target)
        return out