class Solution:
    def mergeTriplets(self, triplets: List[List[int]], target: List[int]) -> bool:
        
        found_a = False
        found_b = False
        found_c = False
        
        for a, b, c in triplets:
            
            if a <= target[0] and b <= target[1] and c <= target[2]:
                
                if a == target[0]: found_a = True
                if b == target[1]: found_b = True
                if c == target[2]: found_c = True
                
        
        return found_a and found_b and found_c