class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        left,right,count=0,0,0
        mychar=set()#zxyzxyz
        while right<len(s):
            while(s[right] in mychar):
                mychar.remove(s[left])
                left+=1
                    
            mychar.add(s[right])
            count = max(count, right - left + 1)
            right+=1
        return count
        