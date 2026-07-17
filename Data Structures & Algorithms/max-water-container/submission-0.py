class Solution:
    def maxArea(self, heights: List[int]) -> int:
        left = 0
        right = len(heights) - 1
        maxArea = 0

        while (left < right):
            height = min(heights[left], heights[right])
            tempArea = (right - left) * height
            if tempArea > maxArea:
                maxArea = tempArea
            else:
                if heights[left] <= heights[right]:
                    left += 1
                else:
                    right -= 1

        return maxArea