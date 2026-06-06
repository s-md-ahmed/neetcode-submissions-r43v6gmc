class Solution:
    def reverse(self,x: int) -> int:
        # Handle the negative sign separately
        sign = -1 if x < 0 else 1
        s = str(abs(x))
    
        # The magic slicing: [start:stop:step]
        reversed_s = s[::-1] 
    
        res = int(reversed_s) * sign
    
        # Check 32-bit range: -2,147,483,648 to 2,147,483,647
        if res < -2**31 or res > 2**31 - 1:
            return 0
        
        return res