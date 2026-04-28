class Solution:
    def getSum(self, a: int, b: int) -> int:
        mask = 0xFFFFFFFF
        
        while b & mask: # While there is still a carry to add
            carry = (a & b) << 1
            a = a ^ b    # Add without carrying
            b = carry    # Make the carry the new 'b' to add next loop
            
        # This part is just to keep Python's infinite numbers in check
        return (a & mask) if b > 0 else a