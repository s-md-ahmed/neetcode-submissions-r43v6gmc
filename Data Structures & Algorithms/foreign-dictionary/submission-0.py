class Solution:
    def foreignDictionary(self, words: list[str]) -> str:
        """
        ========================================================================
        words = ["wrt", "wrf", "er", "ett", "rftt"]
        Here is the exact trace copied over precisely as you requested, completely cleaned of any line numbers:

        ### Phase 1: Going Down the Rabbit Hole (Stack Building)

        Global loop starts at char = 'w'. Calls dfs('w').
        (dfs('w')): 'w' is not in visited. Skip.
        (dfs('w')): visited['w'] = False
        State: visited = {'w': False}
        (dfs('w')): Looks at neighbor = 'e'.
        (dfs('w')): Invokes dfs('e'). dfs('w') is frozen.
        (dfs('e')): 'e' is not in visited. Skip.
        (dfs('e')): visited['e'] = False
        State: visited = {'w': False, 'e': False}
        (dfs('e')): Looks at neighbor = 'r'.
        (dfs('e')): Invokes dfs('r'). dfs('e') is frozen.
        (dfs('r')): 'r' is not in visited. Skip.
        (dfs('r')): visited['r'] = False
        State: visited = {'w': False, 'e': False, 'r': False}
        (dfs('r')): Looks at neighbor = 't'.
        (dfs('r')): Invokes dfs('t'). dfs('r') is frozen.
        (dfs('t')): 't' is not in visited. Skip.
        (dfs('t')): visited['t'] = False
        State: visited = {'w': False, 'e': False, 'r': False, 't': False}
        (dfs('t')): Looks at neighbor = 'f'.
        (dfs('t')): Invokes dfs('f'). dfs('t') is frozen.
        (dfs('f')): 'f' is not in visited. Skip.
        (dfs('f')): visited['f'] = False
        State: visited = {'w': False, 'e': False, 'r': False, 't': False, 'f': False}
        (dfs('f')): Loops over graph['f']. Since it's empty, the loop instantly ends.
        (dfs('f')): visited['f'] = True (Flipped to clean state).
        (dfs('f')): output.append('f')
        State: output = ['f']
        (dfs('f')): Returns True. dfs('f') is popped off the execution stack.

        ---

        ### Phase 2: Unwinding the Stack (The Chain Reaction)

        (dfs('t')): Wakes up! dfs('f') returned True. if not True is false, so it moves past the return check.
        (dfs('t')): No more neighbors left for 't'. The loop terminates.
        (dfs('t')): visited['t'] = True
        (dfs('t')): output.append('t')
        State: output = ['f', 't']
        (dfs('t')): Returns True. dfs('t') is popped off the stack.
        (dfs('r')): Wakes up! dfs('t') returned True. Loop finishes.
        (dfs('r')): visited['r'] = True
        (dfs('r')): output.append('r')
        State: output = ['f', 't', 'r']
        (dfs('r')): Returns True. dfs('r') is popped off the stack.
        (dfs('e')): Wakes up! dfs('r') returned True. Loop finishes.
        (dfs('e')): visited['e'] = True
        (dfs('e')): output.append('e')
        State: output = ['f', 't', 'r', 'e']
        (dfs('e')): Returns True. dfs('e') is popped off the stack.
        (dfs('w')): Wakes up! dfs('e') returned True. Loop finishes.
        (dfs('w')): visited['w'] = True
        (dfs('w')): output.append('w')
        State: output = ['f', 't', 'r', 'e', 'w']
        (dfs('w')): Returns True. dfs('w') finishes completely!

        ---

        ### Phase 3: The Global Loop Clean-up

        Control returns to the main loop:
        Next character is char = 'e'. Calls dfs('e').
        (dfs('e')): Checks if 'e' in visited. True!
        (dfs('e')): return visited['e'] -> Instantly returns True.
        Next character is char = 'r'. Calls dfs('r').
        (dfs('r')): Hits the exact same check, instantly returns True.
        Main loop checks 't', then 'f'. Both hit the check and return True without performing any downstream work.

        The global loop finishes cleanly. The program hits the final wrap-up lines outside the loop, reverses output to get ['w', 'e', 'r', 't', 'f'], and returns "wertf".
        ========================================================================
        """
        # Step 1: Initialize adjacency list for every unique character
        graph = {char: set() for word in words for char in word}
        
        # Step 2: Compare adjacent words to find edge dependencies
        for i in range(len(words) - 1):
            w1, w2 = words[i], words[i + 1]
            min_len = min(len(w1), len(w2))
            
            # Edge Case Check: If w2 is a prefix of w1 but shorter (e.g., "abc" before "ab"), 
            # this is logically impossible in a dictionary. Return empty string.
            if len(w1) > len(w2) and w1[:min_len] == w2[:min_len]:
                return ""
            
            # Find the first mismatching character
            for j in range(min_len):
                if w1[j] != w2[j]:
                    graph[w1[j]].add(w2[j])
                    break # Only the first mismatch gives an ordering rule
                    
        # Step 3: Post-Order DFS to detect cycles and find Topological Order
        # visited dictionary states: False = currently visiting (in current path), True = fully visited
        visited = {}
        output = []
        
        def dfs(char):
            if char in visited:
                return visited[char] # Returns True if safe, False if a loop/cycle is caught
            
            visited[char] = False # Mark as currently visiting (on the recursion stack)
            
            for neighbor in graph[char]:
                if not dfs(neighbor):
                    return False # Cycle detected deep down the path
                    
            visited[char] = True # Mark as fully processed and clean
            output.append(char)   # Post-order append
            return True

        # Run DFS for every character to handle disconnected components
        for char in graph:
            if not dfs(char):
                return "" # If any cycle is detected, configuration is invalid
                
        # Step 4: Reverse the post-order collection to get correct alphabetical sequence
        output.reverse()
        return "".join(output)