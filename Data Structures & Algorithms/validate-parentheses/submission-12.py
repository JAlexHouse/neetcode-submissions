class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        closeToOpen = { ")" : "(", "}" : "{", "]" : "["}
        for c in s:
            if stack and stack[-1] == closeToOpen.get(c, None):
                stack.pop()
            else:
                stack.append(c)
        return not stack
