"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def minMeetingRooms(self, intervals: List[Interval]) -> int:
        out = 0

        intervals.sort(key=lambda i:i.start)

        pq = []

        for interval in intervals:
            if not pq or pq[0] > interval.start:
                # new room required
                heapq.heappush(pq, interval.end)
                out = max(out, len(pq))
            else:
                # next ending room pop
                heapq.heappop(pq)
                heapq.heappush(pq, interval.end)
        return out
            
