class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        mappedNumers = {}
        for idx, num in enumerate(numbers):
            firstIdx = mappedNumers.get(target - num)
            if (firstIdx is not None):
                return [firstIdx, idx + 1]
            else:
                mappedNumers[num] = idx + 1
        return []
