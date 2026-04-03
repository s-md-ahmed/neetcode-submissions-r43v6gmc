class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        n1, n2 = len(s1), len(s2)
        if n1 > n2:
            return False

        target_counts = [0] * 26
        window_counts = [0] * 26

        for i in range(n1):
            target_counts[ord(s1[i]) - ord('a')] += 1
            window_counts[ord(s2[i]) - ord('a')] += 1

        # 3. Check if that very first window was already a match
        if target_counts == window_counts:
            return True

        # 4. START THE SLIDE
        # 'i' is the index of the character ENTERING the window
        for i in range(n1, n2):
            
            right_char_idx = ord(s2[i]) - ord('a')
            window_counts[right_char_idx] += 1

            
            left_char_idx = ord(s2[i - n1]) - ord('a')
            window_counts[left_char_idx] -= 1

            # 5. Compare the arrays after the update
            if target_counts == window_counts:
                return True

        return False