# Definition for an interval.
# class Interval(object):
#     def __init__(self, s=0, e=0):
#         self.start = s
#         self.end = e

class Solution:
    def canAttendMeetings(self, intervals: List[Interval]) -> bool:
        # Sort using the .start attribute of the object
        intervals.sort(key=lambda x: x.start)
        
        for i in range(1, len(intervals)):
            # Compare current start with previous end using attributes
            if intervals[i].start < intervals[i-1].end:
                return False
                
        return True