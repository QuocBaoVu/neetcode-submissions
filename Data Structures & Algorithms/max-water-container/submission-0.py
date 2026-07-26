class Solution:
    def maxArea(self, heights: List[int]) -> int:
        # Brute force: O(N^2)

        # Two pointer greedy:
        p1 = 0
        p2 = len(heights) - 1
        max_area = 0
        while p1 < p2:
            area = (p2-p1) * min(heights[p1], heights[p2])
            max_area = max(max_area, area)
            if heights[p1] < heights[p2]:
                p1 += 1
            else:
                p2 -= 1
        return max_area