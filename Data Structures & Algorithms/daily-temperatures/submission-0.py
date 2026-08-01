class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        # Find next greater, decreasing monotonic stack

        stack = []
        n = len(temperatures)
        out = [0] * n
        for i in range(n):
            while stack and temperatures[i] > temperatures[stack[-1]]:
                curr = stack.pop()
                out[curr] = i - curr
            stack.append(i)
        return out