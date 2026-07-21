class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        stack = []
        solution = [0] * len(temperatures)
        for idx, temp in enumerate(temperatures):
            while stack and temp > stack[-1][0]:
                lesserTemp = stack.pop()
                solution[lesserTemp[1]] = idx - lesserTemp[1]
            stack.append((temp, idx))
        return solution