class Solution:
    def isHappy(self, n: int) -> bool:
        visited = set()
        
       
        while n != 1 and n not in visited:
            visited.add(n)
            n = sum(int(digit) ** 2 for digit in str(n))
            print(n)
            
        return n == 1