class Solution:
    def trap(self, height: List[int]) -> int:
        maxHeight = max(height)
        waterCollected = 0

        for i in range(1, maxHeight + 1):
            startCollecting = False
            tempCollected = 0
            for h in height:
                if h >= i and startCollecting is False:
                    startCollecting = True
                    tempCollected = 0
                elif h < i and startCollecting is True:
                    tempCollected += 1
                elif h >= i and startCollecting is True:
                    waterCollected += tempCollected
                    tempCollected = 0
            
        
        return waterCollected