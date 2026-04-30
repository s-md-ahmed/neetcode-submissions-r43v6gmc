class Solution:
    def merge(self, intervals: list[list[int]]) -> list[list[int]]:
        # --- DRY RUN: intervals = [[4,7],[1,4]] ---
        
        # Step 1: Sort by start time
        # Result: intervals = [[1,4],[4,7]]
        intervals.sort(key=lambda x: x[0])
        
        merged = []
        
        # Step 2: Loop through intervals
        for interval in intervals:
            # ITERATION 1: interval is [1, 4]
            # 'merged' is empty, so 'if not merged' is True.
            # ACTION: merged.append([1, 4])
            # State: merged = [[1, 4]]
            
            # ITERATION 2: interval is [4, 7]
            # 'if not merged' is False.
            # Check overlap: merged[-1][1] is 4. interval[0] is 4.
            # Is 4 < 4? No. So we go to 'else' (overlap detected).
            if not merged or merged[-1][1] < interval[0]:
                merged.append(interval)
            else:
                # ACTION: Update the end of the last interval in merged.
                # merged[-1][1] = max(4, 7) -> which is 7.
                # State: merged = [[1, 7]]
                merged[-1][1] = max(merged[-1][1], interval[1])
            
        # Final Return: [[1, 7]]
        return merged