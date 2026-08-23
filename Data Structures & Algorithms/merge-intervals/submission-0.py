class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort(key=lambda x: x[0])

        output = []

        for interval in intervals:
            if not output or interval[0] > output[-1][1]:
                output.append(interval)
            else:
                output[-1][1] = max(output[-1][1], interval[1])
        return output