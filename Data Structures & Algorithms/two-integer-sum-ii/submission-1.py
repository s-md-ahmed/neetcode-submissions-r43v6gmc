class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        left=0
        right=len(numbers)-1
        currsum=0
        while left<right:
            currsum=numbers[left]+numbers[right]#1,2,3,4,5 target=9
            if currsum>target:
                right-=1
            elif currsum==target:
                break
            else:
                left+=1
        return[left+1,right+1]
            
            