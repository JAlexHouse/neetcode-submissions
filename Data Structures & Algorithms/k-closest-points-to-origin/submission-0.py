class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        distAndCoord = [(math.sqrt((point[0]**2 + point[1]**2)), point) for point in points]
        heapq.heapify(distAndCoord)
        result = []
        for i in range(k):
            if distAndCoord:
                result.append(heapq.heappop(distAndCoord)[1])
        return result