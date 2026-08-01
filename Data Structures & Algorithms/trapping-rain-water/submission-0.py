class Solution:
    def trap(self, height: List[int]) -> int:
        stack = []
        out = 0
        n = len(height)
        for i in range(n):
            while stack and height[i] > height[stack[-1]]:
                curr = stack.pop()
                if not stack:
                    break
                left = stack[-1]
                right = i
                h = min(height[left], height[right])
                w = right - left - 1
                out += (h- height[curr]) * w
            stack.append(i)
        return out


