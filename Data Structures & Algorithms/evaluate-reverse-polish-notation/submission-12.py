class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        # Use a stack to store operands; when we encounter an operator,
        # pop the top two numbers, compute the result, and push it back.
        stack = []
        operators = {'+', '-', '*', '/'}

        for token in tokens:
            # If the token is a number (not an operator), push it onto the stack.
            if token not in operators:
                stack.append(int(token))
                continue

            # At this point, the token is an operator.
            # We operate on the second-to-last and last elements in the stack.
            # stack[-2] is the first operand, stack[-1] is the second operand.
            if token == '+':
                stack[-2] += stack[-1]
                stack.pop()

            elif token == '-':
                stack[-2] -= stack[-1]
                stack.pop()

            elif token == '*':
                stack[-2] *= stack[-1]
                stack.pop()

            else:
                # Division must truncate toward zero, not floor toward negative infinity.
                # Python's '//' is floor division (e.g., -7 // 2 = -4),
                # but the problem expects truncation toward zero (e.g., -7 / 2 = -3).
                # Using int() on true division achieves this by chopping off the decimal part.
                stack[-2] = int(stack[-2] / stack[-1])
                stack.pop()

        # After processing all tokens, the final result is the only element left in the stack.
        return stack[0]