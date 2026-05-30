class Solution:
    def partition(self, s: str) -> list[list[str]]:
        result = []
        
        def isPalindrome(sub: str) -> bool:
            return sub == sub[::-1]
            
        def backtrack(start, current_path):
            
            if start == len(s):
                result.append(list(current_path))
                return
            
            
            for end in range(start + 1, len(s) + 1):
                substring = s[start:end]
                
                
                if isPalindrome(substring):
                    current_path.append(substring)
                    backtrack(end, current_path)
                    current_path.pop() 
        
        backtrack(0, [])
        return result