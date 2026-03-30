class Solution:

    def encode(self, strs: List[str]) -> str:
        enco=""
        for strs1 in strs:
            enco+=str(len(strs1))+'#'+strs1
        return enco
        
    def decode(self, s: str) -> List[str]:
        res, i = [], 0
        
        while i < len(s):
            # 1. Find the '#' (we use j to search ahead)
            j = i
            while s[j] != "#":
                j += 1
            #  5#Hello5#World j=0 j=1 
            # 2. Get the length (all digits between i and j)
            length = int(s[i:j])
            
            # 3. The "Grab": Start after '#' (j+1) for 'length' characters
            word = s[j + 1 : j + 1 + length]
            res.append(word)
            
            # 4. The "Teleport": Move i to the next number
            i = j + 1 + length
            
        return res