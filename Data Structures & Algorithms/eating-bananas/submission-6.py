class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        minK = max(piles)
        piles.sort()
        l, r = 1, max(piles)

        while l <= r:
            mid = l + (r - l) // 2

            currH = sum([math.ceil(x / mid) for x in piles])
            if currH <= h:
                minK = min(minK, mid)
                r = mid - 1
            else:
                l = mid + 1

        return minK

