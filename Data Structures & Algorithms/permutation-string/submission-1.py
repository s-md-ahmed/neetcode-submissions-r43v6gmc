class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        n1, n2 = len(s1), len(s2)
        if n1 > n2: return False
        
        target_counts = [0] * 26
        window_counts = [0] * 26
        
        
        for i in range(n1):
            target_counts[ord(s1[i]) - ord('a')] += 1
            window_counts[ord(s2[i]) - ord('a')] += 1
            
        if target_counts == window_counts:
            return True
        #   s1 = "abc", s2 = "leebca" 
        
        left = 0
        right = n1  # Right starts at the first character OUTSIDE the window
        
        while right < n2:
            
            # Subtract the guy at 'left' because he is leaving
            window_counts[ord(s2[left]) - ord('a')] -= 1
            left += 1  # <--- THERE IT IS! The left moves forward
            
            # Add the guy at 'right' because he is entering
            window_counts[ord(s2[right]) - ord('a')] += 1
            right += 1 # <--- Right moves forward too
            
            # --- THE CHECK ---
            if target_counts == window_counts:
                return True
                
        return False