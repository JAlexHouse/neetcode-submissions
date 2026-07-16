class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        mappedNumers = {}
        for idx, num in enumerate(numbers):
            firstIdx = mappedNumers.get(target - num)
            if (firstIdx is not None):
                print("huh")
                return [firstIdx, idx + 1]
            else:
                print(num)
                mappedNumers[num] = idx + 1
        return []
