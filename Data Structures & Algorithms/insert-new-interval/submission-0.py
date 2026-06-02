class Solution:
    def insert(self, intervals: list[list[int]], newInterval: list[int]) -> list[list[int]]:
        """
        DRY RUN CASES:
        1. NO OVERLAP (Before): intervals=[[1,2]], new=[3,4]
           - Loop 1: Adds [1,2]. Loop 2: No overlap. Loop 3: Adds [3,4]. Result: [[1,2],[3,4]]
        
        2. FULL OVERLAP (Merge): intervals=[[1,5]], new=[2,3]
           - Loop 1: No overlap. Loop 2: Merges [1,5] and [2,3] -> [1,5]. Loop 3: None. Result: [[1,5]]
        
        3. MULTI-MERGE: intervals=[[1,3],[6,9]], new=[2,5]
           - Loop 1: No overlap. Loop 2: 
             - Merge [1,3] & [2,5] -> [1,5]
             - Merge [6,9] & [1,5]? No (4 <= 5 is True, but check 6 <= 5 is False)
           - Loop 3: Adds [6,9]. Result: [[1,5],[6,9]]
        """
        result = []
        i = 0
        n = len(intervals)
        
        # 1. Add everything that ends before the new interval starts
        while i < n and intervals[i][1] < newInterval[0]:
            result.append(intervals[i])
            i += 1
            
        # 2. Merge everything that overlaps
        while i < n and intervals[i][0] <= newInterval[1]:
            newInterval[0] = min(newInterval[0], intervals[i][0])
            newInterval[1] = max(newInterval[1], intervals[i][1])
            i += 1
        result.append(newInterval)
        
        # 3. Add the rest
        while i < n:
            result.append(intervals[i])
            i += 1
            
        return result