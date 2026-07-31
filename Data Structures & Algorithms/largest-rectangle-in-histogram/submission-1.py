class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        out = 0
        heights.append(0)
        n = len(heights)
        stack = []

        for i in range(n):
            while stack and heights[i] < heights[stack[-1]]:
                curr = stack.pop()
                h = heights[curr]
                w = i if not stack else i - stack[-1] - 1
                out = max(out, h*w)
            stack.append(i)
        
        return out