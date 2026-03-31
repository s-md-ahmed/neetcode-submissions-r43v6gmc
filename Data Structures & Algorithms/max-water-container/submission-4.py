class Solution:
    def maxArea(self, heights: List[int]) -> int:
        maxar=0
        left,right=0,len(heights)-1
        while left<right:#[1,2,3,4,5,6,7,8]
            area=min(heights[left],heights[right])*(right-left)
            if maxar<area:
                maxar=area
            if heights[left]<heights[right]:
                left+=1
            else:
                right-=1
        return maxar

        