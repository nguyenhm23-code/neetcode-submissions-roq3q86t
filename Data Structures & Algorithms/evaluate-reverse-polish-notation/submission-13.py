class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        tmp = {'+', '-', '*', '/'}
        for i in tokens:
            if i not in tmp :
                stack.append(int(i))
                continue
            
            if i == '+' :
                stack[-2] += stack[-1] 
                stack.pop()

            elif i == '-' :
                stack[-2] -= stack[-1] 
                stack.pop()

            elif i == '*' :
                stack[-2] *= stack[-1] 
                stack.pop()

            else :
                stack[-2] = int(stack[-2] / stack[-1])
                stack.pop()

        return stack[-1]