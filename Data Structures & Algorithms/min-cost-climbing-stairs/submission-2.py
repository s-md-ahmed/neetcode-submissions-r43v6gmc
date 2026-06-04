'''
Index (i),cost[i] (Original),"Calculation: cost[i] += min(cost[i-1], cost[i-2])",cost[i] (Updated)
0,1,-,1
1,2,-,2
2,1,"1+min(2,1)",2
3,2,"2+min(1,2)",3
4,1,"1+min(2,3)",3
5,1,"1+min(3,3)",4
6,1,"1+min(3,4)",4


'''
class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        
        for i in range(2, len(cost)):
            cost[i] += min(cost[i-1], cost[i-2])
            
        
        return min(cost[-1], cost[-2])