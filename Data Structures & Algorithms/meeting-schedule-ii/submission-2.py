"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def minMeetingRooms(self, intervals: List[Interval]) -> int:
        if len(intervals) == 0: # If there are no meetings, then return 0 because we don't need any rooms to host no meetings (prevents out of range errors later)
                return 0
        intervals.sort(key=lambda interval: interval.start) # Sort intervals by their starting times
        min_heap = [] # Use a min heap to keep track of the earliest ending meeting time because we want to see if we can reuse the room used for the earliest ending meeting for the current meeting
        heapq.heappush(min_heap, intervals[0].end) # Add end time of first meeting to min heap
        for interval in intervals[1:]: # Iterate through list of intervals starting at second interval (we already added the first interval to the min heap)
                if min_heap[0] <= interval.start: # If earliest meeting already ended or ends by the time the current meeting starts, we can reuse the room used for the earliest ending meeting
                        heapq.heappop(min_heap) # Pop the meeting with the earliest end time that doesn't conflict with the current meeting to indicate that we can reuse its room
                heapq.heappush(min_heap, interval.end) # Add the current meeting's end time to the min heap to indicate that it is another room that we need
        return len(min_heap) # After processing all intervals, the number of rooms required to schedule all meetings is the number of elements/meetings in the heap