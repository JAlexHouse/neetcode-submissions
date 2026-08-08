class Solution:
    def trap(self, height: List[int]) -> int:
        l, r = 0, len(height) - 1
        lMax, rMax = height[l], height[r]
        total = 0
        while l < r:
            if lMax < rMax:
                l = l + 1
                lMax = max(height[l], lMax)
                total = total + (lMax - height[l])
            else:
                r = r - 1
                rMax = max(height[r], rMax)
                total = total + (rMax - height[r])
        
        return total
                