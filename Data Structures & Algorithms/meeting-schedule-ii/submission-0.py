import heapq

class Solution:
    def minMeetingRooms(self, intervals: List[Interval]) -> int:
        if not intervals:
            return 0
            
        # 1. Exactly the same as Part 1: Sort by start time
        intervals.sort(key=lambda x: x.start)
        
        # 2. Use a Min-Heap to track end times of meetings currently in rooms
        rooms_heap = []
        
        # Add the first meeting's end time
        heapq.heappush(rooms_heap, intervals[0].end)
        
        for i in range(1, len(intervals)):
            # Check the earliest ending meeting (the top of the heap)
            # If the room is free (start >= earliest end), reuse it
            if intervals[i].start >= rooms_heap[0]:
                heapq.heappop(rooms_heap)
            
            # Always add the current meeting's end time to the heap
            heapq.heappush(rooms_heap, intervals[i].end)
            
        # 3. The size of the heap is the number of rooms we needed
        return len(rooms_heap)