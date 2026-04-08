from collections import Counter

class Solution:
    def minWindow(self, s: str, t: str) -> str:
        need = Counter(t)            
        missing = len(t)             
        start = end = l = 0                        
        min_len = float('inf')
        # s="ABA", t="AA"
        for r, char in enumerate(s):
            # --- EXPAND ---
            if need[char] > 0:       # r=0('A'): 2>0(T) | r=1('B'): 0>0(F)  | r=2('A'): 1>0(T)
                missing -= 1         # r=0: miss=1      | r=1: miss=1       | r=2: miss=0 (VALID!)
            
            need[char] -= 1          # r=0: need[A]=1   | r=1: need[B]=-1   | r=2: need[A]=0

            # --- SHRINK (only runs when missing == 0) ---
            while missing == 0:      # Runs only at r=2
                if r - l + 1 < min_len:
                    min_len = r - l + 1 # r=2, l=0: len=3. min_len = 3
                    start, end = l, r   # start=0, end=2

                # Try to kick out s[l]
                removed_char = s[l]  # l=0: removed='A'
                need[removed_char] += 1 # need['A'] becomes 1

                if need[removed_char] > 0: # 1 > 0 is True
                    missing += 1     # miss=1 (Loop breaks, window no longer valid)
                
                l += 1               # l becomes 1

        # Final Slice: s[0:2+1] -> "ABA"
        return s[start:end+1] if min_len != float('inf') else ""