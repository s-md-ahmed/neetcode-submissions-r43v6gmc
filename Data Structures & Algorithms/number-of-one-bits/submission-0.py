class Solution:
    def hammingWeight(self, n: int) -> int:
        count = 0
        # While there are still '1' bits left in the number
        while n:
            # Check the last bit: if it's 1, add 1 to count
            count += n & 1
            # Shift the number to the right by 1 (shove the bits off the cliff)
            n >>= 1
        return count