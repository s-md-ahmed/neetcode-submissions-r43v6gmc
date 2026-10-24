class Solution:

  def characterReplacement(self, s: str, k: int) -> int:
    # ==========================================
    # CORRECTED DRY RUN TRACE: s = "AABABBA", k = 1
    # Indices: 0='A', 1='A', 2='B', 3='A', 4='B', 5='B', 6='A'
    # ==========================================
    # right=0 ('A'): counts={'A':1}, max_count=1, window="A",     size-max = 1-1=0 <= 1 (True),  res=1
    # right=1 ('A'): counts={'A':2}, max_count=2, window="AA",    size-max = 2-2=0 <= 1 (True),  res=2
    # right=2 ('B'): counts={'A':2,'B':1}, max=2, window="AAB",   size-max = 3-2=1 <= 1 (True),  res=3
    # right=3 ('A'): counts={'A':3,'B':1}, max=3, window="AABA",  size-max = 4-3=1 <= 1 (True),  res=4
    # right=4 ('B'): counts={'A':3,'B':2}, max=3, window="AABAB", size-max = 5-3=2 > 1 (False!)
    #               -> shrink left (left=1): counts['A']=2, window="ABAB", size-max = 4-2=2 > 1 (False!)
    #               -> shrink left (left=2): counts['B']=1, window="BAB",  size-max = 3-2=1 <= 1 (True)
    #               -> res remains 4
    # right=5 ('B'): counts={'A':2,'B':3}, max=3, window="ABABB", size-max = 5-3=2 > 1 (False!)
    #               -> shrink left (left=3): counts['A']=1, window="BABB",  size-max = 4-3=1 <= 1 (True)
    #               -> res remains 4
    # right=6 ('A'): counts={'A':2,'B':3}, max=3, window="BABBA", size-max = 5-3=2 > 1 (False!)
    #               -> shrink left (left=4): counts['B']=2, window="ABBA",  size-max = 4-3=1 <= 1 (True)
    #               -> res remains 4
    # Final Result: 4
    # ==========================================

    left = 0
    max_count = 0
    res = 0
    counts = {}

    for right in range(len(s)):
      counts[s[right]] = 1 + counts.get(s[right], 0)
      max_count = max(max_count, counts[s[right]])

      while (right - left + 1) - max_count > k:
        counts[s[left]] -= 1
        left += 1

      res = max(res, right - left + 1)

    return res