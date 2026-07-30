class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        stack = [] # tuples of (height, index)
        maxArea = 0

        for i, height in enumerate(heights):
            if stack and stack[-1][0] > height:
                pop = None
                while stack and stack[-1][0] > height:
                    pop = stack.pop()
                    area = pop[0] * (i - pop[1])
                    maxArea = max(maxArea, area)
                if pop:
                    stack.append((height, pop[1]))
            elif not stack or stack[-1][0] < height:
                stack.append((height, i))
                
        length = len(heights)
        while stack:
            pop = stack.pop()
            maxArea = max(maxArea, pop[0] * (length - pop[1]))

        return maxArea