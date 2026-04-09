class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        mapping = {')' : '(' , '}' : '{' , ']' : '['}   
        for char in s:
            if char in "([{" :
                stack.append(char)
            elif char in ")]}" and len(stack) > 0 :
                if stack[-1] == mapping[char]:
                    stack.pop()
                elif stack[-1] != mapping[char]:
                    return False
            elif char in ")]}" and len(stack) == 0:
                return False
        if len(stack) < 1:
            return True
        else:
            return False
            


                
