class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        minK = max(piles)
        l, r = 1, minK

        while l < r:
            mid = (l + r) // 2
            currH = sum([math.ceil(x / mid) for x in piles])
            if currH <= h:
                minK = min(mid, minK)
                r = mid
            elif currH > h:
                l = mid + 1
            
        
        return minK