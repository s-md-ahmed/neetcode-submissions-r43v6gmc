class Solution:
    def reverseBits(self, n: int) -> int:
        res = 0
        for _ in range(32):
            # Shift res left to make room for the next bit
            res = (res << 1) | (n & 1)
            # Shift n right to process the next bit
            n >>= 1
        return res