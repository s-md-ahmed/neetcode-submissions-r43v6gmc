class Solution:
    def countBits(self, n: int) -> List[int]:
        # Using a list comprehension + the built-in bit_count() method
        return [i.bit_count() for i in range(n + 1)]