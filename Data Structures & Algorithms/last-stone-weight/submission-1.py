class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        heap = [-stone for stone in stones]
        heapq.heapify(heap)

        while len(heap) > 1:
            stone1, stone2 = -heapq.heappop(heap), -heapq.heappop(heap)
            diff = stone1 - stone2
            if diff > 0:
                heapq.heappush(heap, -diff)
        return 0 if len(heap) == 0 else -heap[0]