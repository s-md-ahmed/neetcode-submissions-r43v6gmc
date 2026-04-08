class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        
        for token in tokens:
            if token in "+-*/":
                # Order matters! Right operand comes off first
                right = stack.pop()
                left = stack.pop()
                
                if token == '+':
                    stack.append(left + right)
                elif token == '-':
                    stack.append(left - right)
                elif token == '*':
                    stack.append(left * right)
                elif token == '/':
                    # int(left / right) handles truncation toward zero
                    stack.append(int(left / right))
            else:
                # It's a number (string), convert to int and push
                stack.append(int(token))
                
        return stack[0]