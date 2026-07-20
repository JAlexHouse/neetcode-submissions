class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        total = 0
        stack = []
        for token in tokens:
            if token.isnumeric() or (token[0] == "-" and token[1:].isnumeric()):
                stack.append(int(token))
            else:
                print(stack, token)
                num2 = stack.pop()
                num1 = stack.pop()
                if token == "+":
                    print(f'add {num1} {num2}')
                    stack.append(num1 + num2)
                if token == "-":
                    print(f'subtract {num1} {num2}')
                    stack.append(num1 - num2)
                if token == "*":
                    print(f'multiply {num1} {num2}')
                    stack.append(num1 * num2)
                if token == "/":
                    print(f'divide {num1} {num2}')
                    stack.append(int(num1 / num2))
        return stack.pop()