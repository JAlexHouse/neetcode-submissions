class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        total = 0
        stack = []
        for token in tokens:
            if token.isnumeric() or (token[0] == "-" and token[1:].isnumeric()):
                stack.append(int(token))
            else:
                num2 = stack.pop()
                num1 = stack.pop()
                if token == "+":
                    stack.append(num1 + num2)
                if token == "-":
                    stack.append(num1 - num2)
                if token == "*":
                    stack.append(num1 * num2)
                if token == "/":
                    stack.append(int(num1 / num2))
        return stack.pop()