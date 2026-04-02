class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        left = 0
        max_count = 0
        res = 0
        counts = {}
        #AAABABB
        for right in range(len(s)):
            counts[s[right]] = 1 + counts.get(s[right], 0)#highest frequcy count
            max_count = max(max_count, counts[s[right]])
            
            while (right - left + 1) - max_count > k:#window size-maxcount of highest to see if it is inside k chars replaceable if true slide the left window in
                counts[s[left]] -= 1
                left += 1
            
            res = max(res, right - left + 1)
            
        return res