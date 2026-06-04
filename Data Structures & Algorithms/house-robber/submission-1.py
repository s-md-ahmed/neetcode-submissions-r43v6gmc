class Solution:
    def rob(self, nums: List[int]) -> int:
        # rob1 = Max money ending 2 houses ago (Grandparent)
        # rob2 = Max money ending 1 house ago (Parent/Neighbor)
        rob1, rob2 = 0, 0
        
        """
        DRY RUN: nums = [2, 9, 8, 3, 6]
        
        1. House = 2:
           temp = max(2 + rob1, rob2) -> max(2 + 0, 0) = 2
           rob1 = 0 (old rob2)
           rob2 = 2 (new max)
           Current State: [rob1=0, rob2=2]
           
        2. House = 9:
           temp = max(9 + rob1, rob2) -> max(9 + 0, 2) = 9
           rob1 = 2 (old rob2)
           rob2 = 9 (new max)
           Current State: [rob1=2, rob2=9]
           
        3. House = 8:
           temp = max(8 + rob1, rob2) -> max(8 + 2, 9) = 10
           rob1 = 9 (old rob2)
           rob2 = 10 (new max)
           Current State: [rob1=9, rob2=10]
           
        4. House = 3:
           temp = max(3 + rob1, rob2) -> max(3 + 9, 10) = 12
           rob1 = 10 (old rob2)
           rob2 = 12 (new max)
           Current State: [rob1=10, rob2=12]
           rob1=rob to keep the houses moving forward if a house is very poor still tmp keeps the highest value that is why we do rob2=temp
        5. House = 6:
           temp = max(6 + rob1, rob2) -> max(6 + 10, 12) = 16
           rob1 = 12 (old rob2)
           rob2 = 16 (new max)
           Current State: [rob1=12, rob2=16]
           
        Final Return: rob2 (16)
        """

        for n in nums:
            # We decide: Current + 2-houses-ago VS 1-house-ago
            temp = max(n + rob1, rob2)
            
            # Slide the variables forward
            rob1 = rob2
            rob2 = temp
            
        return rob2