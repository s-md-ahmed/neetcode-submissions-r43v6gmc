class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        counts={}
        for num in nums:
            counts[num]=1+counts.get(num,0)
        result = sorted(counts, key=counts.get, reverse=True)#sorted(dictionaryname,function utiized,whether to put in descending order if true else ascending)
        return result[:k]


        