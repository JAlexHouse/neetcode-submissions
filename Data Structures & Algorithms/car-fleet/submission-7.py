class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        fleets = 1
        pAndS = list(zip(position, speed))
        pAndS.sort(reverse=True)
        prevTime = (target - pAndS[0][0]) / pAndS[0][1]
        # for s, p in zip(speed, position):
        for p, s in pAndS:
            currTime = (target - p) / s
            if currTime > prevTime:
                fleets += 1
                prevTime = currTime

        return fleets