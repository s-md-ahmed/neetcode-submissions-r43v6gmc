class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        last_idx={}
        for i in range(len(s)):
            last_idx[s[i]]=i
        print(last_idx)
        fin_list=[]
        boundary=0
        start=0
        for i in range(len(s)):
            if last_idx[s[i]]>boundary:
                boundary=last_idx[s[i]]
            if i==boundary:
                fin_list.append(i-start+1)
                start=i+1
        return fin_list

        
        