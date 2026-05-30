class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        if not digits:
            return []
        result=[]
        digit_map = {
            "2": "abc", "3": "def", "4": "ghi", "5": "jkl",
            "6": "mno", "7": "pqrs", "8": "tuv", "9": "wxyz"
        }
        def backtrack(index,current_string):
            if index==len(digits):
                result.append(current_string)
                return
            letters=digit_map[digits[index]]
            for letter in letters:
                backtrack(index+1,current_string+letter)
        backtrack(0,"")
        return result


            
        