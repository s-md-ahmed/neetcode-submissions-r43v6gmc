class Solution:
    def eraseOverlapIntervals(self, intervals: list[list[int]]) -> int:
        
        intervals.sort(key=lambda x: x[1])
        
        count = 0
        
        prev_end = intervals[0][1]
        
        
        for i in range(1, len(intervals)):
            start, end = intervals[i]
            
            if start < prev_end:
                
                count += 1
            else:
                
                prev_end = end
                
        return count