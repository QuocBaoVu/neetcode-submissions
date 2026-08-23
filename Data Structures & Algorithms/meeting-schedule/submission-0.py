"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def canAttendMeetings(self, intervals: List[Interval]) -> bool:
        intervals.sort(key=lambda i: i.start)

        merged = []

        for interval in intervals:
            if not merged or merged[-1].end <= interval.start:
                # non-overlap
                merged.append(interval)
            else:
                return False
        return True