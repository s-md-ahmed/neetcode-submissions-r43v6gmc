from typing import List

class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        # Step 1: Count frequencies
        freq = {}
        for task in tasks:
            freq[task] = freq.get(task, 0) + 1
        
        
        max_freq = max(freq.values())
        max_freq_count = sum(1 for val in freq.values() if val == max_freq)
        print(max_freq_count)
        # Step 3: Calculate the formula
        # (max_freq - 1) * (n + 1) covers the "full" blocks with cooling gaps
        # + max_freq_count adds the final row of tasks that don't need gaps
        result = (max_freq - 1) * (n + 1) + max_freq_count
        
        # Step 4: Return the maximum of the formula or the total tasks
        # If the formula is smaller than the total tasks, it means we don't 
        # have idle time at all, so we just perform the tasks in order.
        return max(result, len(tasks))