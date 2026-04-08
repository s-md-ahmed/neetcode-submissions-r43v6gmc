from collections import Counter

class Solution:
    def minWindow(self, s: str, t: str) -> str:
        """
        DRY RUN: s = "ADOBECODEBANC", t = "ABC" (Goal: Find "BANC")
        
        1. INITIAL: need={A:1, B:1, C:1}, miss=3, l=0, min=inf
        
        2. EXPAND TO FIRST VALID:
           r=0 (A): miss 3->2, need{A:0, B:1, C:1}
           r=3 (B): miss 2->1, need{A:0, B:0, C:1}
           r=5 (C): miss 1->0, need{A:0, B:0, C:0} -> VALID (len 6: "ADOBEC")
           SHRINK: Kick s[0](A), need{A:1}, miss 0->1, l=1. (Exit while)
           
        3. EXPAND TO NEXT VALID:
           r=9 (B): need[B] was 0, now -1. miss stays 1 (Extra B!)
           r=10(A): miss 1->0, need{A:0, B:-1, C:0} -> VALID (len 10: "DOBECODEBA")
           SHRINK: 
             l=1-2: Kick D, O. need stays same, miss stays 0.
             l=3 (B): need[B] -1->0. miss stays 0! (We have the extra B from r=9)
             l=4 (E): Kick E. l=5.
             l=5 (C): need[C] 0->1. miss 0->1. (Exit while, l=6)
             
        4. FINAL STRETCH:
           r=12(C): miss 1->0, need{A:0, B:0, C:0} -> VALID (len 7: "ODEBANC")
           SHRINK:
             l=6-8: Kick O, D, E. need stays same, miss stays 0.
             l=9 (B): len 4 ("BANC") < 6. NEW MIN! start=9, end=12.
             l=9 (B): need[B] 0->1. miss 0->1. (Exit while, l=10)
        """
        
        need = Counter(t)            
        missing = len(t)             
        start = end = l = 0                        
        min_len = float('inf')

        for r, char in enumerate(s):
            # --- EXPAND ---
            if need[char] > 0:       
                missing -= 1
            need[char] -= 1          

            # --- SHRINK ---
            while missing == 0:
                if r - l + 1 < min_len:
                    min_len = r - l + 1
                    start, end = l, r

                removed_char = s[l]
                need[removed_char] += 1
                
                if need[removed_char] > 0:
                    missing += 1
                
                l += 1 

        return s[start:end+1] if min_len != float('inf') else ""