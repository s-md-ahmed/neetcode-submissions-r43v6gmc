class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        left, right, count = 0, 0, 0
        mychar = set()
        
        while right < len(s):
            # If we find a duplicate, shrink window from the left
            while s[right] in mychar:
                mychar.remove(s[left])
                left += 1
            
            # Add the current character and update the record
            mychar.add(s[right])
            count = max(count, right - left + 1)
            
            # Move the scout forward
            right += 1
            
        return count