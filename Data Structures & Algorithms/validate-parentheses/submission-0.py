class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        
        for c in s:
            # Push opening brackets onto the stack
            if c == '(' or c == '[' or c == '{':
                stack.append(c) # Python uses append() instead of push()
            
            # Check for closing brackets
            elif c == ')' and stack and stack[-1] == '(':
                stack.pop()
            elif c == ']' and stack and stack[-1] == '[':
                stack.pop()
            elif c == '}' and stack and stack[-1] == '{':
                stack.pop()
            else:
                return False  # Invalid case
        
        # In the end, the stack should be empty if all brackets are valid
        return len(stack) == 0