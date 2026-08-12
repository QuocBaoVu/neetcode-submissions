class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        out = []
        n = len(nums)
        visited = [False] * n
        def backtrack(path, visited):
            if len(path) == n:
                out.append(path[:])

            for i in range(n):
                if visited[i]:
                    continue
                visited[i] = True
                path.append(nums[i])
                backtrack(path, visited)
                path.pop()
                visited[i] = False
        
        backtrack([], visited)
        return out
