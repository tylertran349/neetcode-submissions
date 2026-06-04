"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def minMeetingRooms(self, intervals: List[Interval]) -> int:
        intervals.sort(key=lambda interval: interval.start) # Sort intervals by their start times so we can process the intervals in chronological order
        min_heap = []
        for interval in intervals:
                heapq.heappush(min_heap, interval.end) # Push current interval's end time onto heap
                if min_heap[0] <= interval.start: # If earliest ending meeting (element at top of heap) ends before or by the time the current interval starts, then the room used for it can be reused by the current interval so remove it from the heap
                        heapq.heappop(min_heap)
        return len(min_heap)