class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        result=[]
        def backtrack(opencount,closecount,current_string):
            if len(current_string) == 2 * n:
                result.append(current_string)
                return
            if opencount<n:
                backtrack(opencount+1,closecount,current_string+"(")
            if opencount > closecount:
                backtrack(opencount,closecount+1,current_string+")")
        backtrack(0,0,"")
        return result
            
