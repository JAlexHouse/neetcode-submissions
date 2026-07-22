class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        cars = list(zip(position, speed))
        cars.sort(reverse=True)
        print(cars)

        fleets = 1
        previousTime = (target - cars[0][0]) / cars[0][1]

        for i in range(1, len(cars)):
            currTime = (target - cars[i][0]) / cars[i][1]
            print(cars[i], "in", currTime, previousTime)
            if (currTime > previousTime):
                fleets += 1
                previousTime = currTime

        return fleets