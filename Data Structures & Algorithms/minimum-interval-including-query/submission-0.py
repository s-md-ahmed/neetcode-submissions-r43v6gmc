import heapq

class Solution:
    def minInterval(self, intervals: list[list[int]], queries: list[int]) -> list[int]:
        """
        Finds the minimum size interval that contains each query.
        
        ========================================================================
        CLEAN DRY RUN (WITH CONDITION EVALUATIONS)
        ========================================================================
        intervals = [[1, 4], [2, 4], [3, 6], [4, 4]]
        queries   = [2, 3, 4, 5]
        
        Sorted Intervals: [[1, 4], [2, 4], [3, 6], [4, 4]]
        Sorted Queries:   [2, 3, 4, 5]
        
        ------------------------------------------------------------------------
        STEP 1: q = 2
        ------------------------------------------------------------------------
        - Add phase loop (Condition: intervals[i][0] <= q):
          * i = 0: [1, 4] -> 1 <= 2 is True  -> Push (size=4, right=4)
          * i = 1: [2, 4] -> 2 <= 2 is True  -> Push (size=3, right=4)
          * i = 2: [3, 6] -> 3 <= 2 is False -> Break loop.
          Heap state: [(3, 4), (4, 4)]
          
        - Clean phase loop (Condition: heap[0][1] < q):
          * Top is (3, 4) -> 4 < 2 is False -> Break loop.
          
        - Grab Best Answer:
          * heap is True -> res[2] = heap[0][0] -> 3
        
        ------------------------------------------------------------------------
        STEP 2: q = 3
        ------------------------------------------------------------------------
        - Add phase loop (Condition: intervals[i][0] <= q):
          * i = 2: [3, 6] -> 3 <= 3 is True  -> Push (size=4, right=6)
          * i = 3: [4, 4] -> 4 <= 3 is False -> Break loop.
          Heap state: [(3, 4), (4, 4), (4, 6)]
          
        - Clean phase loop (Condition: heap[0][1] < q):
          * Top is (3, 4) -> 4 < 3 is False -> Break loop.
          
        - Grab Best Answer:
          * heap is True -> res[3] = heap[0][0] -> 3

        ------------------------------------------------------------------------
        STEP 3: q = 4
        ------------------------------------------------------------------------
        - Add phase loop (Condition: intervals[i][0] <= q):
          * i = 3: [4, 4] -> 4 <= 4 is True  -> Push (size=1, right=4)
          * i = 4: Out of bounds (i < len is False) -> Break loop.
          Heap state: [(1, 4), (3, 4), (4, 4), (4, 6)]
          
        - Clean phase loop (Condition: heap[0][1] < q):
          * Top is (1, 4) -> 4 < 4 is False -> Break loop.
          
        - Grab Best Answer:
          * heap is True -> res[4] = heap[0][0] -> 1

        ------------------------------------------------------------------------
        STEP 4: q = 5
        ------------------------------------------------------------------------
        - Add phase loop (Condition: intervals[i][0] <= q):
          * i = 4: Out of bounds (i < len is False) -> Break loop.
          Heap state remains: [(1, 4), (3, 4), (4, 4), (4, 6)]
          
        - Clean phase loop (Condition: heap[0][1] < q):
          * Top is (1, 4) -> 4 < 5 is True  -> POP (1, 4)
          * Top is (3, 4) -> 4 < 5 is True  -> POP (3, 4)
          * Top is (4, 4) -> 4 < 5 is True  -> POP (4, 4)
          * Top is (4, 6) -> 6 < 5 is False -> Break loop.
          Heap state: [(4, 6)]
          
        - Grab Best Answer:
          * heap is True -> res[5] = heap[0][0] -> 4
        
        ------------------------------------------------------------------------
        Reconstruct original order:
        Return [res[2], res[3], res[4], res[5]] -> [3, 3, 1, 4]
        ========================================================================
        """
        intervals.sort()
        res, heap, i = {}, [], 0
        
        for q in sorted(queries):
            # Phase 1: Add overlapping candidates
            while i < len(intervals) and intervals[i][0] <= q:
                size = intervals[i][1] - intervals[i][0] + 1
                heapq.heappush(heap, (size, intervals[i][1]))
                i += 1
                
            # Phase 2: Discard expired intervals
            while heap and heap[0][1] < q:
                heapq.heappop(heap)
                
            # Phase 3: Record the best valid size
            res[q] = heap[0][0] if heap else -1
            
        return [res[q] for q in queries]