class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        n = len(temperatures)
        finalval = [0] * n
        stack = []
        
        for j in range(n):
            while stack and temperatures[j] > temperatures[stack[-1]]:
                prev_index = stack.pop()
                finalval[prev_index] = j - prev_index
            stack.append(j)
            
        return finalval