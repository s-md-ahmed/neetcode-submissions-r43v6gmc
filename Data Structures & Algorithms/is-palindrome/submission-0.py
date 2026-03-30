class Solution:
    def isPalindrome(self, s: str) -> bool:
        left_pointer = 0
        right_pointer = len(s) - 1
        
        while left_pointer < right_pointer:
            # 1. Skip non-alphanumeric from the left
            while left_pointer < right_pointer and not s[left_pointer].isalnum():
                left_pointer += 1
            
            # 2. Skip non-alphanumeric from the right
            while left_pointer < right_pointer and not s[right_pointer].isalnum():
                right_pointer -= 1
                
            # 3. Compare (case-insensitive)
            if s[left_pointer].lower() != s[right_pointer].lower():
                return False
            
            # 4. Move inward
            left_pointer += 1
            right_pointer -= 1
            
        return True