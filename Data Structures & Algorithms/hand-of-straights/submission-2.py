

class Solution:
    def isNStraightHand(self, hand: List[int], groupSize: int) -> bool:
        """
        ======================================================================
        DRY RUN 1: SUCCESSFUL CASE (Returns True)
        Input: hand = [2, 1, 3, 2, 4, 3], groupSize = 3
        Sorted hand: [1, 2, 2, 3, 3, 4]
        Initial freqmap: {1: 1, 2: 2, 3: 2, 4: 1}

        • card = 1: freqmap[1] is 1 -> Valid start.
          Inner loop keeps `card = 1` constant and runs for i = 0, 1, 2:
          - i = 0 -> curr_card = 1 + 0 = 1: found! count decreases. (freqmap[1] -> 0)
          - i = 1 -> curr_card = 1 + 1 = 2: found! count decreases. (freqmap[2] -> 1)
          - i = 2 -> curr_card = 1 + 2 = 3: found! count decreases. (freqmap[3] -> 1)
          Map state: {1: 0, 2: 1, 3: 1, 4: 1}

        • card = 2: freqmap[2] is 1 -> Valid start.
          Inner loop keeps `card = 2` constant and runs for i = 0, 1, 2:
          - i = 0 -> curr_card = 2 + 0 = 2: found! count decreases. (freqmap[2] -> 0)
          - i = 1 -> curr_card = 2 + 1 = 3: found! count decreases. (freqmap[3] -> 0)
          - i = 2 -> curr_card = 2 + 2 = 4: found! count decreases. (freqmap[4] -> 0)
          Map state: {1: 0, 2: 0, 3: 0, 4: 0}

        • Remaining elements in loop (2, 3, 3, 4) all have counts of 0 -> Skipped!
        • Loop finishes cleanly -> returns True.
        ======================================================================
        
        ======================================================================
        DRY RUN 2: FAILING CASE (Returns False)
        Input: hand = [1, 2, 4], groupSize = 3
        Sorted hand: [1, 2, 4]
        Initial freqmap: {1: 1, 2: 1, 4: 1}

        • card = 1: freqmap[1] is 1 -> Valid start.
          Inner loop keeps `card = 1` constant and runs for i = 0, 1, 2:
          - i = 0 -> curr_card = 1 + 0 = 1: found! count decreases. (freqmap[1] -> 0)
          - i = 1 -> curr_card = 1 + 1 = 2: found! count decreases. (freqmap[2] -> 0)
          - i = 2 -> curr_card = 1 + 2 = 3: freqmap.get(3, 0) returns 0!
                     The number 3 is completely missing from our inventory.
                     *** CASE 3 TRIGGERS HERE *** -> Returns False immediately.
        ======================================================================
        """
        # Early Exit check: If total cards don't fit perfectly into groups
        if len(hand) % groupSize != 0:
            return False
            
        # 1. Sort the hand
        hand.sort()
        
        # 2. Build the frequency map
        freqmap = {}
        for card in hand:
            freqmap[card] = freqmap.get(card, 0) + 1
            
        # 3. Main Loop: Iterate through the sorted hand
        for card in hand:
            
            # CASE 1: Skip completely used-up numbers
            if freqmap[card] == 0:
                continue
                
            # Outer loop found a valid start. Inner loop keeps 'card' value constant:
            for i in range(groupSize):
                curr_card = card + i
                
                # CASE 3: A consecutive number we need is missing or empty
                if freqmap.get(curr_card, 0) == 0:
                    return False
                    
                # CASE 4: Take the card off the table
                freqmap[curr_card] -= 1
                
        return True