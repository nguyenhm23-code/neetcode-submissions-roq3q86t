class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        res = int(tokens[0])
        for i in tokens:
            if i not in ['+', '-', '*', '/'] :
                stack.append(int(i))
                continue
            elif i == '+' :
                res = stack[-1] + stack[-2]
                stack.pop()
                stack.pop()
                stack.append(int(res))
            elif i == '-' :
                res = stack[-2] - stack[-1]
                stack.pop()
                stack.pop()
                stack.append(int(res))
            elif i == '*' :
                res = stack[-1] * stack[-2]
                stack.pop()
                stack.pop()
                stack.append(int(res))
            elif i == '/' :
                res = stack[-2] / stack[-1]
                stack.pop()
                stack.pop()
                stack.append(int(res))
        return int(res)