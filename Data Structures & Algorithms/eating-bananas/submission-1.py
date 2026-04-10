import math

class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        left = 1
        right = max(piles)
        
        
        result = right 
        
        while left <= right:
            mid = (left + right) // 2
            
            
            total_hours = 0
            for p in piles:
                
                total_hours += (p + mid - 1) // mid
                #1+1/2=1
                #1+=4+2-1/2=2
                #3+=3+2-1/2=2
                #5+=2+2-1/2=6
            if total_hours <= h:
                #6<=9 yes result=2
                #right=1
                #1<=1 yes mid=1
                #1
                #1+=4
                #5+=3
                #8+=2
                #10
                #10<=9 false 
                #left=1+1=2 2<=1 false so result stays 2 
                result = mid
                right = mid - 1
            else:
                left = mid + 1
                
        return result