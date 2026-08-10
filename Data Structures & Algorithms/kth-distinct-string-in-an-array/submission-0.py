class Solution:
    def kthDistinct(self, arr: List[str], k: int) -> str:
        counts={}
        for i in arr:
            counts[i]=1+counts.get(i,0)
        a=0
        for i in arr:
            if counts[i]==1:
                a+=1
                if a==k:
                    return i
        return ""
            

        