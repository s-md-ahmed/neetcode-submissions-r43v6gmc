class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        eff_gas = []
        maxim = 0
        best_idx = 0
        i = 0
        while i < len(gas):
            eff_gas.append(gas[i] - cost[i])
            i += 1
        for i in range(len(gas)):
            if eff_gas[i] > maxim:
                maxim = eff_gas[i]
                best_idx = i
                
        # --- NO MORE TALKING, JUST SOLVING WITH THE PERCENT OPERATOR ---
        
        # Quick check: If the total gas available is less than total cost, it's impossible
        if sum(eff_gas) < 0:
            return -1
            
        n = len(gas)
        current_tank = 0
        stations_visited = 0
        test_idx = best_idx  # Start testing from your chosen best_idx

        # Loop through the track using your modulo trick to keep it safe from out-of-bounds
        while stations_visited < n:
            current_tank += eff_gas[test_idx]
            
            # If the tank drops below zero, this starting position (and everything we tested) failed!
            if current_tank < 0:
                # Use the percent operator to shift our candidate to the next station clockwise
                best_idx = (test_idx + 1) % n
                test_idx = best_idx
                current_tank = 0      # Reset tank for the new candidate start
                stations_visited = 0  # Reset counter to make sure the new start can do a full lap
            else:
                # Move to the next station clockwise using the percent operator
                test_idx = (test_idx + 1) % n
                stations_visited += 1

        return best_idx
        