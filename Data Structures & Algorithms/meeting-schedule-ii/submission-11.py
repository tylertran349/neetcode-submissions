"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def minMeetingRooms(self, intervals: List[Interval]) -> int:
        intervals.sort(key=lambda interval: interval.start)
        min_heap = []
        for interval in intervals:
            heapq.heappush(min_heap, interval.end)
            if interval.start >= min_heap[0]:
                heapq.heappop(min_heap)
        return len(min_heap)