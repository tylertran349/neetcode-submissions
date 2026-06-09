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
        min_heap = [] # Min heap to keep track of the earliest ending meeting (we want to see if we can reuse the room used for the earliest ending meeting)
        for interval in intervals:
            heapq.heappush(min_heap, interval.end)
            if min_heap[0] <= interval.start: # If earliest ending meeting ends before or when the current meeting starts, then we can reuse the room used for the earliest ending meeting
                heapq.heappop(min_heap) # Pop the earliest ending meeting time from the heap because we can reuse its room for the current meeting
        return len(min_heap) # Final result is the number of elements in the min heap (represents the number of meetings that need their own separate room)